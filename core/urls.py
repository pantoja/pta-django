from django.urls import path

from .views import HomeView , ContatoView

app_name = 'core'

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('contato/', ContatoView.as_view(), name='contato'),

]