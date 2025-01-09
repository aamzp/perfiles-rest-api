from django.db import models
from django.contrib.auth.models import AbstractBaseUser # AbstractBaseUser is a class that implements the Django User model
from django.contrib.auth.models import PermissionsMixin # PermissionsMixin is a class that implements the Django User model
from django.contrib.auth.models import BaseUserManager # BaseUserManager is a class that implements the Django User model   
from django.conf import settings


''' Creación de modelos de base de datos '''

class UserProfileManager(BaseUserManager):
    '''Gestión para perfiles de usuario'''

    def create_user(self, email, name, password=None):
        '''Crear nuevo usuario'''
        if not email:
            raise ValueError('Usuarios deben tener un email')
        
        email = self.normalize_email(email) # Normaliza el email
        user = self.model(email=email, name=name) # Crea un nuevo usuario

        user.set_password(password) # Encripta la contraseña
        user.save(using=self._db) # Guarda el usuario en la base de datos

        return user
    
    def create_superuser(self, email, name, password):
        '''Crear y guardar un nuevo superusuario'''
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''' Modelo base de datos para usuarios en el sistema'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Obtener nombre completo del usuario'''
        return self.name
    
    def get_short_name(self):
        '''Obtener nombre corto del usuario'''
        return self.name
    
    def __str__(self):
        '''Devuelve cadena representando nuestro usuario'''
        return self.email
    
class ProfileFeedItem(models.Model):
    '''Perfil de status actualizado'''
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Devuelve la representación del modelo en string'''
        return self.status_text