from django.shortcuts import render, redirect, get_object_or_404
from .models import Lector
from .forms import LectorForm

# 1. LEER / BUSCAR (Read)
def listar_lectores(request):
    busqueda = request.GET.get('buscar', '')
    if busqueda:
        # Filtra por nombre completo si se envía el formulario de búsqueda
        lectores = Lector.objects.filter(nombre_completo__icontains=busqueda)
    else:
        # Trae todos los registros de la base de datos
        lectores = Lector.objects.all()
    
    return render(request, 'clientes/listar_lectores.html', {
        'lectores': lectores,
        'busqueda': busqueda
    })


# 2. CREAR (Create)
def crear_lector(request):
    if request.method == 'POST':
        form = LectorForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo lector en la base de datos
            return redirect('listar_lectores')
    else:
        form = LectorForm()
    
    return render(request, 'clientes/crear_lector.html', {'form': form})


# 3. ACTUALIZAR (Update)
def editar_lector(request, pk):
    lector = get_object_or_404(Lector, pk=pk)
    if request.method == 'POST':
        # Carga los datos existentes (instance=lector) y los reemplaza con los nuevos (request.POST)
        form = LectorForm(request.POST, instance=lector)
        if form.is_valid():
            form.save()
            return redirect('listar_lectores')
    else:
        form = LectorForm(instance=lector)
    
    return render(request, 'clientes/editar_lector.html', {
        'form': form, 
        'lector': lector
    })


# 4. ELIMINAR (Delete)
def eliminar_lector(request, pk):
    lector = get_object_or_404(Lector, pk=pk)
    if request.method == 'POST':
        lector.delete()  # Borra el registro de la base de datos
        return redirect('listar_lectores')
    
    return render(request, 'clientes/eliminar_lector.html', {'lector': lector})