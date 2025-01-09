from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Permite a los usuarios editar su propio perfil"""

    def has_object_permission(self, request, view, obj):
        """Chequea si el usuario está intentando editar su propio perfil"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id