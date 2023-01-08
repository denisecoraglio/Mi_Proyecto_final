from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from corrucal.models import Post
from corrucal.forms import UsuarioForm
from corrucal.models import Avatar, Post, Mensaje
from django.contrib.auth.admin import User


@login_required
def index(request):
    posts = Post.objects.order_by('publicado_el').all()
    return render(request, "corrucal/index.html", {"posts": posts})


class PostList(LoginRequiredMixin, ListView):
    model = Post
    
class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("corrucal-listar")
    fields = '__all__'


class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("corrucal-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("corrucal-listar")
    fields = '__all__'

class PostDetalle(DetailView):
    model = Post


class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("corrucal-listar")

class UserLogin(LoginView):
    next_page = reverse_lazy("corrucal-listar")

class UserLogout(LogoutView):
    next_page = reverse_lazy('corrucal-listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy("corrucal-listar")

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy("corrucal-listar")

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("corrucal-mensajes-crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("corrucal-mensajes-listar")

def about(request):
    return render(request, "corrucal/about.html")



    