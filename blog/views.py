from django.shortcuts import render

# Create your views here.
def lista_post(request):
	return render(request, 'blog/lista_post.html',{})