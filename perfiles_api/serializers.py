from rest_framework import serializers

from perfiles_api import models



class HelloSerializer(serializers.Serializer):
    """Serializa un campo para probar nuestra APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializa un objeto de perfil de usuario"""

    class Meta: # Clase Meta para configurar el serializador
        model = models.UserProfile # Modelo a serializar
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = { # Configuración adicional para contrasena
            'password': {
                'write_only': True, # No se muestra en la respuesta
                'style': {'input_type': 'password'} # Tipo de input
            } 
        }
    
    def create(self, validated_data):
        """Crear y retornar un nuevo usuario"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)    
    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializa objetos de perfil de feed"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}} # Configuración adicional para user_profile