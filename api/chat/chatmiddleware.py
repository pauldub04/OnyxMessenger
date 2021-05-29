from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token
from channels.middleware import BaseMiddleware


@database_sync_to_async
def get_user(scope, token_key):
    try:
        token = Token.objects.get(key=token_key)
        print(token.user)
        scope['user'] = token.user
    except Token.DoesNotExist:
        print('No such token')


class TokenAuthMiddleware(BaseMiddleware):

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        token_key = scope['subprotocols'][0]
        scope['user'] = await get_user(scope, token_key)

        return await super().__call__(scope, receive, send)
