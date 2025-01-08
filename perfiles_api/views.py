from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from perfiles_api import serializers


class HelloApiView(APIView):
    """Testeando API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retornar una lista de atributos APIView, algo típico de un get"""

        an_apiview = [
            'métodos HTTP (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la lógica de nuestra aplicación',
            'Está mapeado manualmente a los URLs',


        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):

        """Crea un mensaje con nuestro nombre"""

        serializer = self.serializer_class(data=request.data) # Instancia de la clase HelloSerializer
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name') # Obtiene el nombre del serializer
            message = f'Hello {name}' # Mensaje de respuesta
            return Response({'message': message}) # Retorna el mensaje
        else:
            return Response(
                serializer.errors, # Retorna los errores
                status=status.HTTP_400_BAD_REQUEST # Retorna un error 400
            )
        
    def put(self, request, pk=None):
        """Maneja la actualización de un objeto"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Maneja la actualización parcial de un objeto"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Elimina un objeto"""
        return Response({'method': 'DELETE'})