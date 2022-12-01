from django.forms import modelform_factory
from django.shortcuts import render

from cliente.models import Cliente

#Es para crear un formulario de forma directa. Exclude es para no incluir algún campo de la clase
#cliente en dicho formulario
ClienteForm = modelform_factory(Cliente, exclude=[])


# Create your views here.
def formulario_aniadir_cliente(request):
    mensaje = ''
    if request.method == 'POST':
        try:
            '''
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            dni = request.POST['dni']
            email = request.POST['email']
            print(nombre, apellido, dni, email)
            cliente = Cliente(nombre=nombre, apellidos=apellido, dni=dni, email=email)
            '''
            cliente = ClienteForm(request.POST)
            # Con este comando ya se guarda en Mysql y en admin
            cliente.save()
            mensaje = 'Cliente almacenado correctamente'
        except Exception as e:
            mensaje = f'Error al almacenar el cliente {e}'
        else:
            mensaje = 'Cliente almacenado correctamente'
    else:
        cliente_form = ClienteForm()

    contexto = {'cliente_form':cliente_form, 'mensaje': mensaje}
    return render(request, "insertar_cliente.html", contexto)

# def cliente_add(request):
