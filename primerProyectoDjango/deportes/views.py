from django.shortcuts import render

# Create your views here.
def sports(request):
    diccionario_deportes = {'titulo':'Deportes', 'descripcion':'Los deportes son...'}
    return render(request, "sports.html", diccionario_deportes)