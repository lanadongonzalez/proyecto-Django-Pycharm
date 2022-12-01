from django.shortcuts import render


# Create your views here.
def sports(request):
    diccionario_deportes = {'titulo': 'Deportes', 'descripcion': 'Los deportes son...'}
    return render(request, "sports.html", diccionario_deportes)


def listar_selecciones(request):
    continente_filtro = None
    if request.method == 'POST':
        # es el nombre que hemos puesto en el input del html
        continente_filtro = request.POST['continente']
        # titulo = request.POST('titulo')
        titulo = 'no me sale el get todavia'
    elif request.method == 'GET':
        # Si no funciona el get pondrá por defecto
        # titulo = request.GET('titulo', 'Por defecto')
        titulo = 'no me sale el get todavia'
    # titulo = 'no me sale el get todavia'

    alemania = {'seleccion': 'Alemania', 'continente': 'Europa', 'numero_mundiales': 4}
    brasil = {'seleccion': 'Brasil', 'continente': 'América', 'numero_mundiales': 5}
    japon = {'seleccion': 'Japón', 'continente': 'Asia', 'numero_mundiales': 0}
    ghana = {'seleccion': 'Ghana', 'continente': 'África', 'numero_mundiales': 0}

    lista_selecciones = [alemania, brasil, japon, ghana]
    if (not continente_filtro == None):
        lista_selecciones = list(
            filter(lambda seleccion: seleccion['continente'] == continente_filtro, lista_selecciones))

    contexto = {'listado_selecciones': lista_selecciones,
                'titulo_tabla': titulo}
    return render(request, "gestion/selecciones.html", contexto)

def lista_futbolistas(request):
    return render(request, "gestion/futbolistas.html")
