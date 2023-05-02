from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status


class CursosTestCase(APITestCase): # Teste de integração
    def setUp(self):
        self.list_url = reverse('Cursos-list') # Cria a URL para a listagem
        self.curso_1 = Curso.objects.create( # Cria um curso
            codigo_curso='CTT1', 
            descricao='Curso Teste 1', 
            nivel='B'
        )
        self.curso_2 = Curso.objects.create( # Cria outro curso
            codigo_curso='CTT2',
            descricao='Curso Teste 2',
            nivel='I'
        )

    # def test_falha_listagem_cursos(self):
    #     self.fail('Teste falhou') # Força o teste a falhar

    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar se a requisição GET retorna o status code 200"""
        response = self.client.get(self.list_url) # Faz a requisição GET
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Verifica se o status code é 200]

    def test_requisiscao_post_para_criar_curso(self):
        """Teste para verificar se a requisição POST cria um novo curso"""
        data = { # Dados para criar um novo curso
            'codigo_curso': 'CTT3',
            'descricao': 'Curso Teste 3',
            'nivel': 'B'
        }
        response = self.client.post(self.list_url, data=data) # Faz a requisição POST
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # Verifica se o status code é 201

    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar a requisição DELETE não permitida para deletar um curso"""
        response = self.client.delete('/cursos/1/') # Faz a requisição DELETE
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED) # Verifica se o status code é 405 método não permitido

    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar a requisição PUT atualiza um curso"""
        data = { # Dados para atualizar um curso
            'codigo_curso': 'CTT1',
            'descricao': 'Curso Teste 1 atualizado',
            'nivel': 'I'
        }
        response = self.client.put('/cursos/1/', data=data) # Faz a requisição PUT
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Verifica se o status code é 200
        