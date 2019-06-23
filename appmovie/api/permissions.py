from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


user = get_user_model()


class IsAuthenticatedOrReadOnlyCustom(BasePermission):

    def has_permission(self, request, view):
        return request.method.lower() == 'get' or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method.lower() == 'get' or request.user.is_authenticated
