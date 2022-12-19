from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.

def index(request):
    return render(request, "pages/index/index.html")

def about(request):
    return render(request, "pages/about/about.html")

def gallery(request):
    return render(request, "pages/gallery/gallery.html")

def contact(request):
    return render(request, "pages/contact/contact.html")

def links(request):
    return render(request, "pages/links/links.html")
