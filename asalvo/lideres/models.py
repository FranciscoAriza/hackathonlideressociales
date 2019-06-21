from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Lider(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_doc = models.TextField(max_length=20)
    nro_doc = models.CharField(max_length=60)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    sexo = models.CharField(max_length=20)
    departamento = models.CharField(max_length=150)
    municipio = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)

    nombres_contacto = models.CharField(max_length=150)
    apellidos_contacto = models.CharField(max_length=150)
    telefono_contacto = models.CharField(max_length=20, null=True, blank=True)
    celular_contacto = models.CharField(max_length=20)
    email_contacto = models.EmailField(null=True, blank=True)

    grupo_etnico = models.CharField(max_length=100, null=True, blank=True)
    tipo_liderazgo = models.CharField(max_length=100, null=True, blank=True)
    organizacion_pertenece = models.CharField(max_length=255, null=True, blank=True)

    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True


class DenunciaLider(models.Model):
    situaciones_riesgo = (('001', 'Amenaza propia o familiares'), ('002', 'Asesinato familiares'),
                          ('003', 'Atentado propia o familiares'), ('004', 'Extorsión'),
                          ('005', 'Secuestro propia o familiares'), ('006', 'Otra'))
    medios_hecho = (('01', 'Telefónico'), ('02', 'Escrito'), ('03', 'Verbal'), ('04','Terceros'))
    presuntos_autores = (('01', 'Bandas criminales'), ('02', 'Empresas'), ('03', 'EPL'), ('04', 'ELN'),
                         ('05', 'Disidencias de las FARC'), ('06', 'Paramilitares'), ('07', 'Particulares'), ('08', 'Fuerza Pública'))
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    departamento_denuncia = models.TextField(max_length=100)
    municipio_denuncia = models.TextField(max_length=100)
    situacion_riesgo = models.CharField(max_length=100, choices=situaciones_riesgo, default="006")
    departamento_hecho = models.TextField(max_length=100)
    municipio_hecho = models.TextField(max_length=100)
    fecha_hecho = models.DateField()
    medio = models.TextField(max_length=100, choices=medios_hecho, default="01")
    presunto_autor = models.TextField(max_length=100, choices=presuntos_autores, default="01")
    descripcion = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to='audios/', null=True, blank=True)

    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True


class Denuncia(models.Model):
    situaciones_riesgo = (('001', 'Amenaza propia o familiares'), ('002', 'Asesinato familiares'),
                          ('003', 'Atentado propia o familiares'), ('004', 'Extorsión'),
                          ('005', 'Secuestro propia o familiares'), ('006', 'Otra'))
    medios_hecho = (('01', 'Telefónico'), ('02', 'Escrito'), ('03', 'Verbal'), ('04','Terceros'))
    presuntos_autores = (('01', 'Bandas criminales'), ('02', 'Empresas'), ('03', 'EPL'), ('04', 'ELN'),
                         ('05', 'Disidencias de las FARC'), ('06', 'Paramilitares'), ('07', 'Particulares'), ('08', 'Fuerza Pública'))
    departamento_denuncia = models.TextField(max_length=100)
    municipio_denuncia = models.TextField(max_length=100)
    situacion_riesgo = models.CharField(max_length=100, choices=situaciones_riesgo, default="006")
    departamento_hecho = models.TextField(max_length=100)
    municipio_hecho = models.TextField(max_length=100)
    fecha_hecho = models.DateField()
    medio = models.TextField(max_length=100, choices=medios_hecho, default="01")
    presunto_autor = models.TextField(max_length=100, choices=presuntos_autores, default="01")
    descripcion = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to='audios/')

    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True