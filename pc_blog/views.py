from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import pc_post
from django.views.generic import ListView, CreateView
from django.template import loader 





def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
    
 
def details(request, id):
    memb = pc_post.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'memb': memb,
    }    
    return HttpResponse(template.render(context, request))
    

class mypc(ListView):
    model = pc_post
    template_name = 'pc.html'
