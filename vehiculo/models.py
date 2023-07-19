from django.db import models

# Create your models here.

class VehiculoModel(models.Model):
    
    nMarca= (
        ('Chevrolet','Chevrolet'),
        ('Fiat','Fiat'),
        ('Ford','Ford'),
        ('Toyota', 'Toyota'),        
    )
    
    nCategoria= (
        ('Particular','Particular'),
        ('Transporte','Transporte'),
        ('Carga','Carga'),
    )
    
    marca= models.CharField(max_length=100, choices=nMarca, default ='Ford') 
    modelo= models.CharField(max_length=100)
    serial_carroceria= models.CharField(max_length=50)
    serial_motor= models.CharField(max_length=50)
    categoria= models.CharField(max_length=20, choices=nCategoria, default ='Particular')
    precio=models.IntegerField()
    clasificacion=models.CharField(max_length=20, blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_modificacion=models.DateTimeField(auto_now=True)
    
        
    class Meta:
        verbose_name = "vehiculo"
        verbose_name_plural="vehiculos"
        ordering=["-fecha_creacion"]
        permissions = (
            ("visualizar_catalogo","Visualizar catálogo"),
        )
    
    def __str__(self):
        return self.marca
    
    def save(self, *args,**kwargs):
        if self.precio <=10000:
            self.clasificacion='Bajo'
        elif self.precio <= 30000:
            self.clasificacion = 'Medio'
        else:
            self.clasificacion='Alto'
        super().save(*args,**kwargs)    
        
    def __str__(self):
        return self.marca

    