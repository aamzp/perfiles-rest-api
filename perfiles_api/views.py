from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from perfiles_api import serializers
from perfiles_api import models
from perfiles_api import permissions

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
    

class HelloViewSet(viewsets.ViewSet):
    """Testeando ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Retorna un mensaje simple"""
        a_viewset = [
            'Usa acciones (list, create, retrieve, update, partial_update)',
            'Automáticamente mapea a los URLs usando Routers',
            'Provee más funcionalidad con menos código',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Crea un nuevo mensaje"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Maneja la obtención de un objeto por su ID"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Maneja la actualización de un objeto"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Maneja la actualización parcial de un objeto"""
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Elimina un objeto"""
        return Response({'http_method': 'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Maneja la creación y actualización de perfiles de usuario"""
    serializer_class = serializers.UserProfileSerializer # Instancia de la clase UserProfileSerializer
    queryset = models.UserProfile.objects.all() # Queryset de todos los perfiles de usuario
    authentication_classes = (TokenAuthentication,) # Autenticación por token
    permission_classes = (permissions.UpdateOwnProfile,) # Permisos de actualización de perfil
    filter_backends = (filters.SearchFilter,) # Filtro de búsqueda
    search_fields = ('name', 'email',) # Campos de búsqueda

class UserLoginApiView(ObtainAuthToken):
    """Maneja la creación de tokens de autenticación"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES # Renderiza la respuesta