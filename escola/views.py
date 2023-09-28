from rest_framework import viewsets
from escola.models import Aluno, Curso
from .serializer import AlunoSerializer, CursoSerializer

class AlunosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset =  Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer