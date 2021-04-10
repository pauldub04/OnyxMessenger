"""Views for the chat app."""

from django.contrib.auth import get_user_model
from .models import (
    ChatSession, ChatSessionMember, ChatSessionMessage, deserialize_user
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class ChatSessionView(APIView):
    """Manage Chat sessions."""

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """create a new chat session."""
        user = request.user

        chat_session = ChatSession.objects.create(owner=user)

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
            if len(messages) == 0:
                messages = [{'user': {'id': -1, 'username': '', 'email': '', 'first_name': '', 'last_name': ''},
                             'message': 'No messages yet'}]

            sessions.append({
                'uri': c.uri,
                'username': '',
                'userImage': '',
                'lastMessage': messages[-1]['message'],
                'unreadMessages': 0,
                'messages': messages
            })

        return Response({
            'status': 'SUCCESS',
            'sessions': sessions,
        })

    def patch(self, request, *args, **kwargs):
        """Add a user to a chat session."""
        User = get_user_model()

        uri = kwargs['uri']
        username = request.data['username']

        try:
            user = User.objects.get(username=username)
        except:
            return Response({
                'status': 'ERROR',
                'message': 'No such username',
            })

        chat_session = ChatSession.objects.get(uri=uri)
        if user in [chat_session.user for chat_session in chat_session.members.all()]:
            return Response({
                'status': 'ERROR',
                'message': 'User is already in chat',
            })

        owner = chat_session.owner
        inviter_user = request.user

        # Only allow non owners join the room
        if owner != user and inviter_user == owner:
            chat_session.members.get_or_create(
                user=user,
                chat_session=chat_session,
            )

            owner = deserialize_user(owner)
            members = [deserialize_user(chat_session.user) for chat_session in chat_session.members.all()]

            members.insert(0, owner)  # Make the owner the first member
            return Response({
                'status': 'SUCCESS', 'members': members,
                'message': '%s joined that chat' % user.username,
                'user': deserialize_user(user)
            })
        else:
            return Response({
                'status': 'ERROR',
                'message': 'Only owner now can invite',
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

        return Response({
            'id': chat_session.id, 'uri': chat_session.uri,
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