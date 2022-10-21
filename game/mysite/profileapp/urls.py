from django.urls import path
from .views import ProfileView, GameView

#Creating ProfileView, ArticleView, CreatePostView, etc... for the ease of a view

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('game', GameView.as_view(), name='game'),
]