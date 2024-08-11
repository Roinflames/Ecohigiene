# views.py


from django.shortcuts import render
import os
from django.conf import settings

def home(request):
    img_folder = os.path.join(settings.STATICFILES_DIRS[0], 'img')
    print(f"Ruta de la carpeta de imágenes: {img_folder}")  # Depuración
    image_files = [f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f))]
    print(f"Archivos encontrados: {image_files}")  # Depuración
    context = {
        'images': image_files
    }
    return render(request, 'home.html', context)


def datos(request):

    return render(request, 'datos.html')


def contenedor(request):

    return render(request, 'contenedores.html')


