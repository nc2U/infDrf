from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Post, Comment, Category, Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PostListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'title', 'image', 'like', 'category', 'create_dt']


class PostRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        exclude = ['create_dt']


class PostSerializerSub(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title')


class CommentInPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'update_dt')


class PostDetailSerializer(serializers.Serializer):
    post = PostRetrieveSerializer()
    prevPost = PostSerializerSub()
    nextPost = PostSerializerSub()
    commentList = CommentInPostDetailSerializer(many=True)


# class PostLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['like']


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
