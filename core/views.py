from django.shortcuts import render
from django.views import generic
from .models import Posts

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse  
from django.urls import reverse_lazy
from templated_email import send_templated_mail

class HomeView(generic.TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Posts.objects.all()
        return context

class ContatoView(generic.TemplateView):
    template_name = 'core/contato.html'
    def post (self,request, *args, **kwargs):
        print('teste')
        nome=request.POST.get('nome')
        email=request.POST.get('email')
        telefone=request.POST.get('telefone')
        assunto=request.POST.get('assunto')
        mensagem=request.POST.get('mensagem')
        send_templated_mail(
        template_name='email',
        from_email= email,
        recipient_list=['ptaprojetos.contato@gmail.com'],
        context={
            'nome':nome,
            'email':email,
            'telefone':telefone,
            'assunto':assunto,
            'mensagem':mensagem
        },)
        print('teste2')
        return HttpResponseRedirect(reverse_lazy("core:contato"))