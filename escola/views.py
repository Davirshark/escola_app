from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, AlunoPorCpfSerializer, ListaMatriculasAlunoSerializer,ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class AlunosViewsSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
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

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer

class AlunoPorCpfViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Aluno.objects.filter(cpf = self.kwargs['pk'])
        return queryset
    serializer_class = AlunoPorCpfSerializer

class BuscaAlunosPorNome(generics.CreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def get_queryset(self):
        nome = self.request.data.get('nome', '')
        return Aluno.objects.filter(nome__icontains=nome)
    
class BuscaAlunosPorNome(APIView):
    def post(self, request, format=None):
        print (request)
        if request.data  == None:
            return Response(Aluno.objects.all())
        nome = request.data.get('nome', '')
        alunos = Aluno.objects.filter(nome__icontains=nome)
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data) 
    
class DeletarAluno(APIView):
    def delete(self, request, id, format=None):
        try:
            aluno = Aluno.objects.get(pk=id)
        except Aluno.DoesNotExist:
            return Response({'Aluno não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        aluno.delete()
        return Response({'Aluno excluído com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
           