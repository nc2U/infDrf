# from rest_framework import viewsets
# from django.contrib.auth.models import User
#
# from apiV2.serializers import UserSerializer, PostSerializer, CommentSerializer
# from blog.models import Post, Comment
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     CreateAPIView, GenericAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from apiV2.serializers import (PostListSerializer, PostRetrieveSerializer,
                               CommentSerializer, CateTagSerializer)
from blog.models import Post, Comment, Category, Tag


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer


# class PostLikeAPIView(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostLikeSerializer
#
#     # PATCH method
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         data = { 'like': instance.like + 1 }
#         serializer = self.get_serializer(instance, data=data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         if getattr(instance, '_prefetched_objects_cache', None):
#             instance._prefetched_objects_cache = {}
#
#         return Response(serializer.data['like'])


class PostLikeAPIView(GenericAPIView):
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        return Response(instance.like)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CateTagAPIView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        cate_list = Category.objects.all()
        tag_list = Tag.objects.all()
        data = {
            'cateList': cate_list,
            'tagList': tag_list,
        }
        serializer = CateTagSerializer(instance=data)
        return Response(serializer.data)
