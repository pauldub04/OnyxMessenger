"""Views for the chat app."""
import json

from django.contrib.auth import get_user_model
from .models import (
    ChatSession, ChatSessionMember, ChatSessionMessage, deserialize_user, User
)
from rest_framework import viewsets

from .consumers import ChatConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class ChatSessionView(APIView):
    """Manage Chat sessions."""

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """create a new chat session."""
        global new_u
        user = request.user

        chat_type = int(request.data['type'])
        users = json.loads(request.data['users'])
        title = request.data['title']
        image = request.data['image']

        chat_session = ChatSession.objects.create(owner=user, title=title, type=(chat_type - 1), image=image)

        print(chat_type, users, title)
        for u in users:
            find = list(User.objects.filter(username=u))
            if find:
                new_u = find[0]
                chat_session.members.get_or_create(
                    user=new_u,
                    chat_session=chat_session,
                )
            else:
                print('no user with username', u)

        return Response({
            'status': 'SUCCESS', 'uri': chat_session.uri,
            'message': 'New chat session created'
        })

    def get(self, request, *args, **kwargs):
        """get all chat sessions of user."""

        user = request.user

        chat_sessions = []
        chat_sessions_all = list(ChatSession.objects.all())

        for c in chat_sessions_all:
            if user in [c.user for c in c.members.all()] or c.owner == user:
                chat_sessions.append(c)

        sessions = []
        for c in chat_sessions:
            messages = [chat_session_message.to_json() for chat_session_message in c.messages.all()]

            chat_users = [c.user for c in c.members.all()]
            members = [{
                'username': c.owner.username,
                'type': 'owner',
            }]
            for m in chat_users:
                members.append({
                    'username': m.username,
                    'type': 'user',
                })

            sessions.append({
                'uri': c.uri,
                'username': '',
                'userImage': '',
                'lastMessage': messages[-1]['message'] if len(messages) > 0 else 'No messages yet',
                'unreadMessages': 0,
                'messages': messages,
                'title': c.title,
                'members': members,
                'image': str(c.image)
            })

        return Response({
            'status': 'SUCCESS',
            'sessions': sessions,
        })

    def patch(self, request, *args, **kwargs):
        """Add a user to a chat session."""
        User = get_user_model()

        uri = kwargs['uri']
        chat_session = ChatSession.objects.get(uri=uri)

        owner = chat_session.owner
        if request.user != owner:
            return Response({
                'status': 'ERROR',
                'message': 'Only owner now can invite',
            })

        username = request.data['username']
        try:
            user = User.objects.get(username=username)
        except:
            return Response({
                'status': 'ERROR',
                'message': 'No such username',
            })

        if user == owner:
            return Response({
                'status': 'ERROR',
                'message': 'You can not invite yourself',
            })

        if user in [chat_session.user for chat_session in chat_session.members.all()]:
            return Response({
                'status': 'ERROR',
                'message': user.username + ' is already in chat',
            })

        chat_session.members.get_or_create(
            user=user,
            chat_session=chat_session,
        )
        members = [deserialize_user(chat_session.user) for chat_session in chat_session.members.all()]
        members.insert(0, deserialize_user(owner))  # Make the owner the first member

        return Response({
            'status': 'SUCCESS', 'members': members,
            'message': '%s joined that chat' % user.username,
            'user': deserialize_user(user)
        })


class UsersView(APIView):
    """Manage Users."""

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """get all users."""

        users_list = list(User.objects.all())

        users = []
        for u in users_list:
            users.append(u.username)

        return Response({
            'status': 'SUCCESS',
            'users': users,
        })


class ChatSessionMessageView(APIView):
    """Create/Get Chat session messages."""

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """return all messages in a chat session."""
        uri = kwargs['uri']

        chat_session = ChatSession.objects.get(uri=uri)
        messages = [chat_session_message.to_json()
                    for chat_session_message in chat_session.messages.all()]
        owner = chat_session.owner

        chat_members = [c.user for c in chat_session.members.all()]
        usernames = [{
            'username': owner.username,
            'type': 'owner',
        }]
        for m in chat_members:
            usernames.append({
                'username': m.username,
                'type': 'user',
            })

        return Response({
            'id': chat_session.id, 'uri': chat_session.uri,
            'members': usernames,
            'messages': messages
        })

    def post(self, request, *args, **kwargs):
        """create a new message in a chat session."""
        uri = kwargs['uri']
        message = request.data['message']

        user = request.user
        chat_session = ChatSession.objects.get(uri=uri)

        ChatSessionMessage.objects.create(
            user=user, chat_session=chat_session, message=message
        )

        return Response({
            'status': 'SUCCESS', 'uri': chat_session.uri, 'message': message,
            'user': deserialize_user(user)
        })
