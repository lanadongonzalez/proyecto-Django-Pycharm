from django.shortcuts import render
from django.forms import modelform_factory
from deportes.models import Futbolista


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
    futbolistas = Futbolista.objects.all()
    # filtro = {'posicion': [], 'nacionalidad': [], 'equipo': []}
    filtro_posicion = []
    filtro_nacionalidad = []
    filtro_equipo = []

    # Vamos a meter los valores en un diccionario para filtra según esos valores
    for jugador in futbolistas:
        if jugador.posicion not in filtro_posicion:
            filtro_posicion.append(jugador.posicion)
        if jugador.nacionalidad not in filtro_nacionalidad:
            filtro_nacionalidad.append(jugador.nacionalidad)
        if jugador.equipo not in filtro_equipo:
            filtro_equipo.append(jugador.equipo)

    if request.method == 'POST':
        accion = request.POST.get('action', '')
        if accion == 'filtrar':
            posicion_filtrada = request.POST['posicion']
            print(posicion_filtrada)
            nacionalidad_filtrada = request.POST['nacionalidad']
            equipo_filtrada = request.POST['equipo']
            futbolistas_tabla = list(filter(
                lambda futbolista: futbolista.posicion == posicion_filtrada and futbolista.nacionalidad == nacionalidad_filtrada and futbolista.equipo == equipo_filtrada,
                futbolistas))
        else:
            futbolistas_tabla = futbolistas
    else:
        futbolistas_tabla = futbolistas
    context = {'futbolistas': futbolistas_tabla, 'filtro_posicion': filtro_posicion,
               'filtro_nacionalidad': filtro_nacionalidad, 'filtro_equipo': filtro_equipo}
    return render(request, "gestion/futbolistas.html", context)


FutbolistaForm = modelform_factory(Futbolista, exclude=[])


def add_futbolista(request):
    mensaje = ''
    if request.method == 'POST':
        try:
            futbolista_form = FutbolistaForm(request.POST)
            futbolista_form.save()
        except Exception as e:
            mensaje = f'Error al almacenar el futbolista {e}'
        else:
            mensaje = "Futbolista almacenado correctamente"

    futbolista_form = FutbolistaForm()

    contexto = {"futbolista_form": futbolista_form, "mensaje": mensaje}
    return render(request, "gestion/add_futbolista.html", contexto)
