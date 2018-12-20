from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action

from app_user.serializers import UserSerializer, GroupSerializer
# from fa_core import permissions
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# Admin
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


# API
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = User.objects.order_by('-date_joined')
    #     serializer = UserSerializer(queryset, many=True, context={'request': request})
    #     data = serializer.data
    #     return Response(data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset,pk = kwargs.get('pk'))
    #     serializer = UserSerializer(user, context={'request': request})
    #     data = serializer.data
    #     return Response(data)
    @action(methods=['get'], detail=True, permission_classes=[permissions.AllowAny, ])
    def validate_username(self, request, pk=None):
        is_taken = User.objects.filter(username__iexact=pk).exists()
        return Response({'is_taken': is_taken})

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer