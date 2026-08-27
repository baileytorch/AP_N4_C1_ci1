# AP_N4_C1_ci1
Clases de Backend con Django

## Creación de Proyectos con Django

1. **Creación de Ambiente Virtual**
    - Un ambiente virtual mantendrá asilada toda la configuración de nuestro proyecto y su entorno de trabajo.- Habiendo creado nuestro repositorio, abrimos la carpeta contenedora en VS Code.</li>
    - Estando ubicados en el directorio principal, iniciamos un nuevo terminal.</li>
    - Para crear el ambiente virtual, ejecutamos el siguiente comando en el terminal:
    ```
    python -m venv nombre_ambiente
    ```
    
2. **Activación de Ambiente Virtual**
    - Mediante el terminal accedemos al directorio creado anteriormente, ejecutando el siguiente comando:
    ```
    cd nombre_ambiente\Scripts
    ```
    - Para activar el ambiente virtual, ejecutamos el siguiente comando en el terminal:
    ```
    .\Activate
    ```
    - Si no se puede ejecutar el comando, debemos darle permisos al terminal, mediante el siguiente comando:
    ```
    Set-ExecutionPolicy Bypass -Scope CurrentUser
    ```
    - Habiendo ejecutado este comando, ya deberíamos poder ejecutar el comando anterior y activar nuestro ambiente virtual.
    - Si necesitamos desactivar el ambiente virtual, usaremos el comando:
    ```
    deactivate
    ```

3. **Actualización de PIP**
    - A pesar de haber generado un instalación del entorno desde 0, no está asegurado que contenga la última versión de PIP, por lo que debemos actualizarlo.
    - Para actualizarlo, ejecutamos el siguiente comando en nuestro terminal:
    ```
    python -m pip install --upgrade pip
    ```

4. **Instalación de Entorno Django**
    - Mediante terminal nos ubicamos en el directorio raíz de la aplicación.
    - Una vez ubicado el terminal en el directorio raíz, ejecutaremos el siguiente comando:
    ```
    pip install django
    ```
    - El comando anterior instaló todas las dependencias necesarias para que Django pueda trabajar.
    - Crearemos el entorno de trabajo de Django mediante el comando:
    ```
    django-admin startproject motor_django .
    ```
    - Este comando creó la estructura de archivos de Django, es un directorio que contiene los archivos de configuración. 
        - settings.py, contiene configuraciones generales, como la conexión a base de datos.
        - urls.py, contiene las rutas para redirigir las solicitudes que lleguen a la aplicación.

5. **Creación de la Aplicación**
    - Para crear la aplicación que debemos construir, ejecutaremos el siguiente comando mediante terminal:
    ```
    django-admin startapp nombre_aplicacion
    ```
    - Cuando la estructura de archivos de la aplicación a construir ya ha sifo generada, ya podemos iniciar la el servidor de la aplicación, ejecutando el siguiente comando en el terminal:
    ```
    python manage.py runserver
    ```
    - Este comando inicia el servidor, el que se carga en la url http://127.0.0.1:8000.

6. **Modificando la página de inicio**
    - Por defecto cuando iniciamos el servidor carga una página con información de Django, pero no es lo que debiéramos ver cuando cargamos una aplicación, por lo que cambiaremos la página de inicio.
    - Primero debemos indicarle a Django que el directorio de nuestra aplicación contiene una APP, agregamos nuestra APP a la lista INSTALLED_APPS  de Django/settings.py:
    ```
    INSTALLED_APPS = [
        # apps de django
        'mi_app',
    ]
    ```

    - Luego debemos importar las vistas desde nuestra app en Django/urls.py y llamar al método que renderizará esa vista:
    ```
    from mi_app import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.bienvenida, name='bienvenida'),
    ]
    ```

    - En el archivo mi_app/views.py generamos el método que renderizará la vista:
    ```
    def bienvenida(request):
        return render(request, 'bienvenida.html')
    ```

    - Finalmente, en nuestra app creamos un directorio templates, donde pondremos nuestras vistas.
    - Dentro de mi_app/templates creamos la vista HTML que será renderizada por el método creado anteriormente.
    - Cuando iniciemos nuevamente nuestro servidor, debiera cargar la vista recién creada en lugar de la vista Django por defecto.

7. **Página de Error 404 Genérica**
    - Si python NO encuentra un recurso (página) solicitado para cargar, arrojará una página de error con información del servidor