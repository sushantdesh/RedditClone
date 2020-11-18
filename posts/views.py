from django.shortcuts import render
from .serializers import PostSerializer
from .models import Posts

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.request import Request
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = PostSerializer
    def get_queryset(self):
        param=self.request.GET.get('param','')
        if param=='':
            return Posts.objects.all().order_by('-upvote')
        else:
            return Posts.objects.all().order_by(param)

    def perform_create(self, serializer):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipadd = x_forwarded_for.split(',')[0]
        else:
            ipadd = self.request.META.get('REMOTE_ADDR')
        serializer.save(owner=self.request.user, ip=ipadd)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Posts.objects.all()
    serializer_class = PostSerializer



class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, post=Posts.objects.get(id=self.request.data['id']))
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer






# @api_view(["GET"])
# # @permission_classes([IsAuthenticated])
# def getComments(request):
#     queryset=Comment.objects.all()
#     serializer_class = CommentSerializer(queryset, many=True)
#     return Response({'Comments':serializer_class.data}, status=status.HTTP_200_OK)
#
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def postComment(request):
#     serializer = CommentSerializer(data=request.data,context={'request': Request(request)})
#     if serializer.is_valid():
#         serializer.save()
#     #     print(serializer.data)
#     # else:
#     #     print(serializer.errors)
#     # newdict = {'postedby': request.user.username}
#     # newdict.update(serializer.data)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#
# @api_view(["GET"])
# # @permission_classes([IsAuthenticated])
# def getPosts(request):
#     queryset=Posts.objects.all()
#     serializer_class = PostSerializer(queryset, many=True)
#     return Response({'posts':serializer_class.data}, status=status.HTTP_200_OK)
#
# @api_view(["GET"])
# # @permission_classes([IsAuthenticated])
# def getDetailedPost(request,pk):
#     queryset=Posts.objects.get(id=pk)
#     serializer_class = PostSerializer(queryset, many=False)
#     return Response({'posts':serializer_class.data}, status=status.HTTP_200_OK)
#
#
#
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def createPost(request):
#     serializer=PostSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#









