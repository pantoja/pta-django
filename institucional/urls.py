from django.urls import path

from .views import InstitucionalView 

app_name = 'institucional'

urlpatterns = [
  path('', InstitucionalView.as_view(), name='institucional'),

]