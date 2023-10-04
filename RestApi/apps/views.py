from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .serializers import UserSerializer,RegisterSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView
#Register_Api

class RegisterApi(generics.GenericAPIView):
    serializer_class=RegisterSerializer

    def post(self,request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@api_view(['DELETE'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def get_user(request, pk):
    user = User.objects.filter(pk=pk)
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)