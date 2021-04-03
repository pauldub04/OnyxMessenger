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
        chat_sessions = list(ChatSession.objects.filter(owner=user))

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
        user = User.objects.get(username=username)

        chat_session = ChatSession.objects.get(uri=uri)
        owner = chat_session.owner

        if owner != user:  # Only allow non owners join the room
            chat_session.members.get_or_create(
                user = user, chat_session = chat_session
            )

        owner = deserialize_user(owner)
        members = [
        deserialize_user(chat_session.user)
        for chat_session in chat_session.members.all()

        ]

        members.insert(0, owner)  # Make the owner the first member
        return Response({
            'status': 'SUCCESS', 'members': members,
            'message': '%s joined that chat' % user.username,
            'user': deserialize_user(user)
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