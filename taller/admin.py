from django.contrib import admin
from .models import Pais, Region, Provincia, Comuna, Direccion
from .models import Biblioteca, Autor, Genero,SubGenero,Editorial
from .models import Idioma,Edicion,Libro,Estado,Ubicacion,Inventario,Usuario,Prestamo

# Register your models here.
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Biblioteca)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(SubGenero)
admin.site.register(Editorial)
admin.site.register(Idioma)
admin.site.register(Edicion)
admin.site.register(Libro)
admin.site.register(Estado)
admin.site.register(Ubicacion)
admin.site.register(Inventario)
admin.site.register(Usuario)
admin.site.register(Prestamo)