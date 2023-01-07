"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView 
from ejemplo.views import mostrar_cursos, mostrar_alumnos, mostrar_tutores
from ejemplo.views import *
from corrucal.views import (index, PostList,
                             PostCrear, PostDetalle, PostBorrar, PostActualizar, UserSignUp, UserLogin,
                             UserLogout, AvatarActualizar)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/', mostrar_cursos),
    path('cursos/buscar', BuscarCurso.as_view()),
    path('cursos/alta', AltaCurso.as_view()),
    path('cursos/actualizar/<int:pk>', ActualizarCurso.as_view()),
    path('cursos/borrar/<int:pk>', BorrarCurso.as_view()),
    path('alumnos/', mostrar_alumnos),
    path('alumnos/alta', AltaAlumnos.as_view()),
    path('alumnos/actualizar/<int:pk>', ActualizarAlumno.as_view()),
    path('alumnos/borrar/<int:pk>', BorrarAlumno.as_view()),
    path('tutores/', mostrar_tutores),
    path('tutores/alta', AltaTutores.as_view()),  
    path('tutores/actualizar/<int:pk>', ActualizarTutor.as_view()),
    path('tutores/borrar/<int:pk>', BorrarTutor.as_view()),
    path('panel-curso/', CursoList.as_view()),
    path('panel-curso/crear', CursoCrear.as_view()),
    path('panel-curso/<int:pk>/borrar', CursoBorrar.as_view()),
    path('panel-curso/<int:pk>/actualizar', CursoActualizar.as_view()),
    path('panel-curso/<int:pk>/detalle', CursoDetalle.as_view()),
    path('success_update_message/', TemplateView.as_view(template_name="ejemplo/success_update_message.html")),
    path('corrucal/', index, name= 'corrucal-index'),
    path('corrucal/listar/', PostList.as_view(), name = 'corrucal-listar'),
    path('corrucal/crear/', staff_member_required(PostCrear.as_view()), name = 'corrucal-crear'),
    path('corrucal/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name = 'corrucal-borrar'),
    path('corrucal/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name = 'corrucal-actualizar'),
    path('corrucal/<int:pk>/detalle/', PostDetalle.as_view(), name = 'corrucal-detalle'),
    path('corrucal/signup/', UserSignUp.as_view(), name ="corrucal-signup"),
    path('corrucal/login/', UserLogin.as_view(), name ="corrucal-login"),
    path('corrucal/logout/', UserLogout.as_view(), name="corrucal-logout"),
    path('corrucal/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="corrucal-avatars-actualizar"),


]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)