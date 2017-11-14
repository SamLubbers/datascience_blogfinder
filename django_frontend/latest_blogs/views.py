from django.shortcuts import render
from .models import Blogs

def index(request):
    latest_blogs = Blogs.objects.order_by('-pub_date')[:100]
    context = {"latest_blogs": latest_blogs}
    return render(request, 'latest_blogs/blogs.html', context)
