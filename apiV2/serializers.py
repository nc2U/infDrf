from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Post, Comment, Category, Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'title', 'image', 'like', 'category']


class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['create_dt']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['like']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CateInCateTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class TagInCateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


# class CateTagSerializer(serializers.Serializer):
#     cate_list = CateInCateTabSerializer(many=True)
#     tag_list = TagInCateTagSerializer(many=True)


class CateTagSerializer(serializers.Serializer):
    cateList = serializers.ListField(child=serializers.CharField())
    tagList = serializers.ListField(child=serializers.CharField())
