from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Testeando API View"""

    def get(self, request, format=None):
        """Retornar una lista de atributos APIView, algo típico de un get"""

        an_apiview = [
            'métodos HTTP (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la lógica de nuestra aplicación',
            'Está mapeado manualmente a los URLs',
            

        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})