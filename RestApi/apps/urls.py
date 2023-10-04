from .views import RegisterApi,UserListView,delete_user
from django.urls import path
from . import views

urlpatterns=[
    path("user/register/",RegisterApi.as_view(),name="user"),
    path("user/all_users/",UserListView.as_view(),name="all_users"),
    path('user/<int:pk>/delete/', views.delete_user, name='delete-user'),
    path("user/<int:pk>/",views.get_user, name="user")
    
]