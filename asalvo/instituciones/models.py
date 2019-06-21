from django.db import models

# Create your models here.
class GVP(models.Model):
    ano = models.SmallIntegerField()
    ot = models.IntegerField()
    tipo_estudio_riesgo = models.TextField(max_length=100)
    matriz_estudio = models.FloatField()
    nivel_de_riesgo = models.CharField(max_length=150)
    decision = models.TextField()
    concepto = models.TextField()
    sintesis = models.TextField()
    orden_publico = models.TextField(null=True)
    dpto_reparto_riesgo = models.CharField(max_length=150)
    mun_reparto_riesgo = models.CharField(max_length=150)
    sintesis_hechos_1 = models.TextField(null=True, blank=True)
    sintesis_hechos_2 = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class Meta:
    managed = True


class Amenaza(models.Model):
    ano = models.SmallIntegerField()
    ot = models.IntegerField()
    dpto_riesgo = models.CharField(max_length=150)
    mun_riesgo = models.CharField(max_length=150)
    tipo_estudio_riesgo = models.TextField(max_length=100)
    genero = models.TextField(max_length=100)
    nivel_de_riesgo = models.CharField(max_length=150)
    sintesis_hechos_gvp = models.TextField()
    desicion_gvp = models.TextField()
    dpto_residencia = models.CharField(max_length=150)
    mun_residencia = models.CharField(max_length=150)
    grupo_poblacional = models.CharField(max_length=150)
    observaciones = models.TextField(null=True)
    sinopsis_informacion = models.TextField(null=True)
    carac_presun_amenaza = models.TextField(null=True)
    analisis_info = models.TextField(null=True)
    sintesis_1 = models.TextField(null=True, blank=True)
    sintesis_2 = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class Meta:
    managed = True
