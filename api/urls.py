from django.urls import path

from api import views


urlpatterns = [
    path('posts', views.PostListAndCreate.as_view(),
         name='list and create posts'),
    path('posts/<int:pk>', views.PostDetailUpdateDelete.as_view(),
         name='list, update and delete posts'),
    path('comments', views.CommentListAndCreate.as_view(),
         name='list and create comments'),
    path('comments/<int:pk>', views.CommentDetail.as_view(),
         name='list, update and delete comments'),
]
