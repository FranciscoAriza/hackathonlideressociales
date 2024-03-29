# Generated by Django 2.2.2 on 2019-06-21 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lideres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento_denuncia', models.TextField(max_length=100)),
                ('municipio_denuncia', models.TextField(max_length=100)),
                ('situacion_riesgo', models.CharField(choices=[('001', 'Amenaza propia o familiares'), ('002', 'Asesinato familiares'), ('003', 'Atentado propia o familiares'), ('004', 'Extorsión'), ('005', 'Secuestro propia o familiares'), ('006', 'Otra')], default='006', max_length=100)),
                ('departamento_hecho', models.TextField(max_length=100)),
                ('municipio_hecho', models.TextField(max_length=100)),
                ('fecha_hecho', models.DateField()),
                ('medio', models.TextField(choices=[('01', 'Telefónico'), ('02', 'Escrito'), ('03', 'Verbal'), ('04', 'Terceros')], default='01', max_length=100)),
                ('presunto_autor', models.TextField(choices=[('01', 'Bandas criminales'), ('02', 'Empresas'), ('03', 'EPL'), ('04', 'ELN'), ('05', 'Disidencias de las FARC'), ('06', 'Paramilitares'), ('07', 'Particulares'), ('08', 'Fuerza Pública')], default='01', max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('audio', models.FileField(upload_to='audios/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DenunciaLider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento_denuncia', models.TextField(max_length=100)),
                ('municipio_denuncia', models.TextField(max_length=100)),
                ('situacion_riesgo', models.CharField(choices=[('001', 'Amenaza propia o familiares'), ('002', 'Asesinato familiares'), ('003', 'Atentado propia o familiares'), ('004', 'Extorsión'), ('005', 'Secuestro propia o familiares'), ('006', 'Otra')], default='006', max_length=100)),
                ('departamento_hecho', models.TextField(max_length=100)),
                ('municipio_hecho', models.TextField(max_length=100)),
                ('fecha_hecho', models.DateField()),
                ('medio', models.TextField(choices=[('01', 'Telefónico'), ('02', 'Escrito'), ('03', 'Verbal'), ('04', 'Terceros')], default='01', max_length=100)),
                ('presunto_autor', models.TextField(choices=[('01', 'Bandas criminales'), ('02', 'Empresas'), ('03', 'EPL'), ('04', 'ELN'), ('05', 'Disidencias de las FARC'), ('06', 'Paramilitares'), ('07', 'Particulares'), ('08', 'Fuerza Pública')], default='01', max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to='audios/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
