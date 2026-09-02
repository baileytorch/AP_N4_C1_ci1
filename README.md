# AP_N4_C1_ci1
Clases de Backend con Django

Como buenos desarrolladores, ya debemos tener creado un repositorio para trabajar el código de la aplicación que debemos construir.
    - Si no ha trabajado aún con repositorios, he construido una pequeña guía paso a paso que está disponible en sus ambientes de aprendizaje.
    - El proyecto que debe construir cada uno se ha asignado con anterioridad y puede encontrar la información en su ambiente de aprendizaje.

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