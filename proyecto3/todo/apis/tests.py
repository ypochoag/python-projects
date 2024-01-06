from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from todos.models import Todo
from .serializers import TodoSerializer
import json


class TodoViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.my_model_data = {
            "titulo": "test",
            "descripcion": "test1",
            "estado": "pendiente"
        }
        self.my_model = Todo.objects.create(**self.my_model_data)

    def test_list_get(self):
        response = self.client.get('/apis/v1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        response = self.client.post('/apis/v1/', data=self.my_model_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put(self):
        update_data = {'titulo': "test1",
                       "descripcion": "test1",
                       "estado": "pendiente"}
        url = f"/apis/v1/{self.my_model.id}/"
        response = self.client.put(url, data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        url = f"/apis/v1/{self.my_model.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    

    def test_validar_serializador_con_datos_validos(self):
        serializer = TodoSerializer(data=self.my_model_data)
        self.assertTrue(serializer.is_valid())

    def test_validar_serializador_con_datos_no_validos(self):
        data = {"titulo": "test",
                "descripcion": "test1",
                "estado": "_"}
        serializer = TodoSerializer(data=data)
        self.assertFalse(serializer.is_valid())
