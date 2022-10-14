from django.urls import path

from authentication import views

urlpatterns = [
    path('', views.UserAuthenticationView.as_view(), name='home page'),
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('list', views.UserListView.as_view(), name='list user'),
    path('list/<int:pk>', views.UserListDetail.as_view(), name='list user detail'),
]
