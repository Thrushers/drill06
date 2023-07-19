from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import VehiculoForm, RegistroUsuarioForm
from tokenize import PseudoExtras
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import VehiculoModel

# Create your views here.

def indexView(request):
    context={
        'user_junior':request.user.has_perm('vehiculo.visualizar_catalogo'),
        'user_senior':request.user.has_perm('vehiculo.add_vehiculomodel'),
        
    }
    return render(request,'index.html', context)

def addVehiculo(request):
    if request.user.has_perm('vehiculo.add_vehiculomodel'):
        
        form = VehiculoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            form = VehiculoForm()
            messages.success(request, '¡Los datos se han procesado exitosamente!')
           
        
        return render(request,'addform.html',{'form':form,'user_junior':request.user.has_perm('vehiculo.visualizar_catalogo'),'user_senior':request.user.has_perm('vehiculo.add_vehiculomodel')})
    else:
        return HttpResponseRedirect('index/')
      
def menuView(request):
    context= {}
    return render(request, 'menu.html', context)

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(VehiculoModel)
            visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo',content_type=content_type)
            
            user=form.save()
            user.user_permissions.add(visualizar_catalogo)
            login(request, user)
            messages.success(request, "Usuario registrado exitosamente")
            return HttpResponseRedirect('/')
        messages.error(request,"Registro invalido, uno o mas datos son incorrectos, favor verificar")
    
    form = RegistroUsuarioForm()
    context={ "register_form":form}
    return render(request, "registro.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste secion como: {username}")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Username o Password invalido!")
        else:
            messages.error(request, "Username o Password invalido!")
    
    form = AuthenticationForm()
    context={ "login_form":form}
    return render(request, "login.html", context) 

def logout_view(request):
    logout(request)
    messages.success(request,"Se ha cerrado sesión satisfactoriamente!")
    return HttpResponseRedirect('/')
     
def listar_vehiculo(request):
    if request.user.has_perm('vehiculo.visualizar_catalogo'):
        vehiculos = VehiculoModel.objects.all()
        context = {'lista_vehiculos': vehiculos,'user_junior':request.user.has_perm('vehiculo.visualizar_catalogo'),'user_senior':request.user.has_perm('vehiculo.add_vehiculomodel')}
        return render(request, 'lista.html',context)
    else:
        return HttpResponseRedirect('index/')


