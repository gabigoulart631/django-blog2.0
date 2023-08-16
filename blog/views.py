from django.shortcuts import render
from blog.models import Post

from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

def ola(request):
  #return HttpResponse('Olá, Django')
# return render(request, 'home.html')
  posts = Post.objects.all() # recupera todos os posts do banco de dados
  context = {'posts_list': posts } # cria um dicionário com os dado
  return render(request, 'posts.html', context) # renderiza o template e passa o contexto