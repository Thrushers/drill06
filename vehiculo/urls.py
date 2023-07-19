from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name='index'),
    path('addform/', addVehiculo ,name='addform'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view , name='login'),
    path('logout/', logout_view, name='logout'),
    path('listar/', listar_vehiculo, name ='listar'),
    
]
