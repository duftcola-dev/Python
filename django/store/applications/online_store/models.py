from django.db import models

# Create your models here.
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------

class Empleado(models.Model):
    """Tabla empleado model"""
    JOB_CHOICES =(
        ('0','MANAGER'),
        ('1','EMPLEADO'),
        ('2','CONTABLE'),
    )
    nombre = models.CharField("nombre",max_length=20,null=False)
    apellido= models.CharField("apellido",max_length=20,null=False)
    rol=models.CharField("roles",max_length=1,choices=JOB_CHOICES,null=False)

    def __str__(self):
        return str(self.id)+" "+self.first_name+" "+self.second_name+" "+self.job
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
   
        indexes=[
            models.Index(fields=['rol'],name='idx_empleado_rol'),
            models.Index(fields=['nombre','rol'],name='idx_empleado_nombre_rol'),
            models.Index(fields=['nombre'],name='idx_empleado_nombre'),
        ]
    
    def __str__(self):
        return str(self.id)+" "+self.nombre+" "+self.apellido+" "+self.role

#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------

class Manager(models.Model):
    """Tabla mananager"""
    nombre= models.OneToOneField(Empleado,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"
        indexes=[
            models.Index(fields=['nombre'],name='idx_manager_nombre'),
            models.Index(fields=['id','nombre'],name='idx_manager_id_nombre'),
        ]
    
    def __str__(self):
        return str(self.id)+" "+self.nombre

#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------

class Tienda(models.Model):
    """Tabla tienda"""

    TYPE_CHOICES = (
        ('0','consumo'),
        ('1','electronica'),
        ('2','moda'),
        ('3','deporte'),
    )
    nombre_tienda = models.CharField("nombre",max_length=20,null=False)
    tipo_tienda = models.CharField("tipo_tienda",max_length=1,choices=TYPE_CHOICES)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    manager = models.OneToOneField(Manager,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"
        unique_together=('nombre_tienda','manager') # a combination of store and manager must be unique
        
        indexes=[ 
            models.Index(fields=['id','nombre_tienda'],name='idx_tienda_id_nombre_tienda'),
            models.Index(fields=['empleado'],name='idx_tienda_empleado'),
            models.Index(fields=['manager'],name='idx_tienda__manager'),
            models.Index(fields=['id','nombre_tienda',"tipo_tienda","empleado","manager"],name='idx_tienda_id_s_e_m'),
        ]

    def __str__(self):
        return str(self.id)+" "+self.nombre_tienda+" "+self.tipo_tienda+" "+self.empleado+" "+self.manager

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------


