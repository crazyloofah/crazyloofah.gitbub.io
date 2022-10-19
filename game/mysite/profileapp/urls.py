from django.urls import path
from .views import ProfileView

#Creating ProfileView, ArticleView, CreatePostView, etc... for the ease of a view

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
]