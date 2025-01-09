## Introducción
Este proyecto es una API RESTful construida con Django y Django REST framework. Proporciona endpoints para gestionar perfiles de usuario, autenticación y otras funcionalidades.

## Requisitos previos

1. Tener Vagrant operativo para este proyecto con la terminal en la carpeta raiz
    ```bash
    vagrant init ubuntu/bionnic64
    ```
    ```bash
    vagrant up
    ```
    ```bash
    vagrant ssh
    ```
    ```bash
    cd/vagrant
    ```
    ```bash
    source ~/env/bin/activate
    ```
## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>
    ```

2. **Crear y activar un entorno virtual**:
    ```bash
    python -m venv venv
    ~/env/bin/activate
    ```

3. **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Aplicar migraciones**:
    ```bash
    python manage.py migrate
    ```

5. **Crear un superusuario**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Iniciar el servidor de desarrollo**:
    ```bash
    python manage.py runserver
    ```

## Endpoints

### Hello API View
- **URL**: `/hello-view/`
- **Métodos**: `GET`, `POST`
- **Descripción**: 
  - `GET`: Retorna una lista de atributos de la API View.
  - `POST`: Crea un mensaje con el nombre proporcionado.

### Hello ViewSet
- **URL**: `/hello-viewset/`
- **Métodos**: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- **Descripción**: Maneja las operaciones CRUD para el viewset de prueba.

### User Profile
- **URL**: `/perfil/`
- **Métodos**: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- **Descripción**: Maneja la creación, actualización y eliminación de perfiles de usuario.

### User Login
- **URL**: `/login/`
- **Métodos**: `POST`
- **Descripción**: Autentica a un usuario y retorna un token de autenticación.

## Administración de Django
Para acceder a la administración de Django, ve a `/admin/` en tu navegador y usa las credenciales del superusuario que creaste.
e.
