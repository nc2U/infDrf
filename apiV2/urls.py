# from django.urls import path, include
# from rest_framework import routers
#
# from apiV2.views import UserViewSet, PostViewSet, CommentViewSet
#
# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comment', CommentViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path

from apiV2.views import *

urlpatterns = [
    path('post/', PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostRetrieveAPIView.as_view(), name='post-detail'),
    path('comment/', CommentCreateAPIView.as_view(), name='comment-list'),
]
