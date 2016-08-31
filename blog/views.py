from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
# Create your views here.


def lista_post(request):
	post = Post.objects.filter(fecha_publicada__lte=timezone.now()).order_by('fecha_publicada')
	return render(request, 'blog/lista_post.html',{'posts': post})

def detalle_post(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request, 'blog/detalle_post.html',{'post':post})

def nuevo_post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.fecha_publicada = timezone.now()
			post.save()
			return redirect('blog.views.detalle_post',pk=post.pk)
	else:
		form = PostForm()
	

	return render(request,'blog/edita_post.html', {'form': form})

def edita_post(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post) 
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.save()
		return redirect('blog.views.detalle_post',pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request,'blog/edita_post.html',{'form':form})