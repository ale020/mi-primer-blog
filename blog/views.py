from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.


def lista_post(request):
	post = Post.objects.filter(fecha_publicada__lte=timezone.now()).order_by('fecha_publicada')
	return render(request, 'blog/lista_post.html',{'posts': post})

