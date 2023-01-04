from django.shortcuts import render
from django.views.generic import ListView, CreateView
from corrucal.models import Post
from django.urls import reverse_lazy


def index(request):
    return render(request, "corrucal/index.html", {} )


class PostList(ListView):
    model = Post
    
class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("corrucal-listar")
    fields = '__all__'
