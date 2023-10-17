"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from escola.views import AlunosViewsSet, AlunoPorCpfViewSet, CursosViewsSet, MatriculasViwesSet, ListaMatriculasAluno, ListaAlunosMatriculados, BuscaAlunosPorNome, DeletarAluno
from rest_framework import routers
from clientes.views import ClientesViewSet


router = routers.DefaultRouter()
router.register('alunos', AlunosViewsSet, basename='Alunos')
router.register('cursos', CursosViewsSet, basename='Cursos')
router.register('matriculas', MatriculasViwesSet, basename='Matriculas')
router.register('clientes', ClientesViewSet)





urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas', ListaAlunosMatriculados.as_view()),   
    path('alunoPorCpf/<int:pk>', AlunoPorCpfViewSet.as_view()),
    path('buscaAlunos/', BuscaAlunosPorNome.as_view()),
    path('deletarAluno/<int:id>', DeletarAluno.as_view())
]

