from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from corrucal.models import Post
from corrucal.forms import UsuarioForm
from corrucal.models import Avatar


@login_required
def index(request):
    return render(request, "corrucal/index.html", {} )


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

class PostDetalle(LoginRequiredMixin, DetailView):
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



    