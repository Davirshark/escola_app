from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, AlunoPorCpfSerializer, ListaMatriculasAlunoSerializer,ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

class AlunosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset =  Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViwesSet(viewsets.ModelViewSet):
    """Exibindo todo os alunos"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]  
    permission_classes = [IsAuthenticated]

class AlunoPorCpfViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Aluno.objects.filter(cpf = self.kwargs['pk'])
        return queryset
    serializer_class = AlunoPorCpfSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]  