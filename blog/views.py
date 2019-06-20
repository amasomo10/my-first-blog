from django.shortcuts import render
from django.utils import timezone
from .models import Post #dot before models means current directory or application
                          #... no .py needed at the models
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
