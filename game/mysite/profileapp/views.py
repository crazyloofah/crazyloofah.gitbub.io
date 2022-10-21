from django.views.generic import ListView
from .models import BlogPost


#We pull our forms from '''.forms''' and put them into our views for us to connect
#Creating ProfileView, ArticleView, CreatePostView, etc... for the ease of a view

class ProfileView(ListView):
    model = BlogPost 
    template_name = 'profile.html'

class GameView(ListView):
    model = BlogPost
    template_name = 'game.html'


    



   

