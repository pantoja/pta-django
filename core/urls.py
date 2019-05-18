from django.urls import path

from .views import HomeView, ContatoView, CreatePostView

app_name = 'core'

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('contato/', ContatoView.as_view(), name='contato'),
  path('post/', CreatePostView.as_view(), name='create-post'),
]