from django.db import models

class Lector(models.Model):
    # 1. CharField: Para texto
    nombre_completo = models.CharField(max_length=100)
    # 2. IntegerField: Para números enteros
    numero_socio = models.IntegerField(unique=True)
    # 3. DateTimeField: Para guardar la fecha y hora exacta
    fecha_registro = models.DateTimeField(auto_now_add=True)
    # 4. BooleanField: Para saber si es verdadero o falso
    cuota_al_dia = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre_completo} - Socio: {self.numero_socio}'