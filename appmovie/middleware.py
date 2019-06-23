from django.contrib.auth.models import User
from appmovie.models import Token


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_anonymous:
            token = request.META.get('HTTP_AUTHORIZATION', '')
            try:
                if Token.objects.filter(token=token).exists():
                    data = Token.objects.get(token=token)
                    request.user = data.user
            except Exception:
                pass
            response = self.get_response(request)
            return response
        response = self.get_response(request)
        return response
