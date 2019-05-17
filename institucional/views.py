from django.shortcuts import render
from .models import Institucional
from django.views.generic import (
    TemplateView
)



class InstitucionalView(TemplateView):
    template_name = 'institucional/institucional.html'
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        if(len(Institucional.objects.all()) > 0):
            context['Institucional'] = Institucional.objects.all()[0]
        return context 
