from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset =  Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class CursosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViwesSet(viewsets.ModelViewSet):
    """Exibindo todo os alunos"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer