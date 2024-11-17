from django.contrib import admin
from .models import Libros

# Register your models here.
@admin.register(Libros)

class LibrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'precio', 'fecha_p')
    search_fields = ('titulo', )
