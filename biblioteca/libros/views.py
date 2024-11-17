from django.shortcuts import render
from .models import Libros
from django.db.models import Count

# Create your views here.
def registro_libros(request):
    if request.method == 'POST':
        titulo = request.POST.get ('titulo')
        autor = request.POST.get ('autor')
        categoria = request.POST.get ('categoria')
        precio = request.POST.get ('precio')
        fecha_p = request.POST.get ('fecha_p')
        
        Libros.objects.create(
            titulo = titulo,
            autor = autor,
            categoria = categoria,
            precio = precio,
            fecha_p = fecha_p
            )
        
    return render(request, 'libros/registrar_libros.html')

def analytics(request):
    #consulta el número de libros por categoría
    libros_por_categoria = Libros.objects.values('categoria').annotate(count = Count('id'))
    
    #consulta los 5 autores con más publicaciones
    top_autores = Libros.objects.values('autor').annotate(count = Count('id')).order_by('-count')[:5]
        
    return render(request, 'analytics.html', {'libros_por_categoria': libros_por_categoria, 'top_autores': top_autores})