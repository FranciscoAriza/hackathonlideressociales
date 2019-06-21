from django import forms
from .models import Lider, DenunciaLider

class AcreditarLiderForm(forms.ModelForm):
    class Meta:
        model = Lider
        fields = ('usuario','tipo_doc', 'nro_doc', 'nombres', 'apellidos', 'sexo', 'departamento',
              'municipio', 'telefono', 'celular', 'email', 'nombres_contacto', 'apellidos_contacto',
              'telefono_contacto', 'celular_contacto', 'email_contacto', 'grupo_etnico', 'tipo_liderazgo',
                'organizacion_pertenece')
    #     exclude = ('valor',)
        tipo_doc_choices = [('CC','Cédula de ciudadania'), ('CE', 'Cédula de extranjeria'), ('PS', 'Pasaporte'), ('TI', 'Tarjeta de identidad')]
        sexo_choices = [('M','Masculino'), ('F', 'Femenino'), ('Otro', 'Otro'), ('No', 'No especificar')]
        grupo_etnico_choices = [('Afrocolombiano', 'Afrocolombiano'), ('Indigena', 'Indigena'), ('Negro', 'Negro'),
                            ('Palanquero', 'Palanquero'), ('Rom o Gitano', 'Rom o Gitano'), ('Sordo Raizal', 'Sordo Raizal')]
        tipo_liderazgo_choices = [('Activista político', 'Activista político'), ('Defensa derechos de la mujer', 'Defensa derechos de la mujer'),
                                  ('Defensa derechos comunidades afro', 'Defensa derechos comunidades afro'),
                                  ('Defensa derechos comunidades indígenas', 'Defensa derechos comunidades indígenas'),
                                  ('Defensa derechos campesinos', 'Defensa derechos campesinos'),
                                  ('Defensa derechos LGBTI', 'Defensa derechos LGBTI'), ('Líder reclamante', 'Líder reclamante'),
                                  ('Sindicato', 'Sindicato'), ('Otro', 'Otro')]

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'hidden': True}),
            'tipo_doc': forms.Select(attrs={'class': 'form-control', 'required': True}, choices=tipo_doc_choices),
            'nro_doc': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'sexo': forms.Select(attrs={'class': 'form-control', 'required': True}, choices=sexo_choices),
            'departamento': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'municipio': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'telefono': forms.TextInput(attrs={'class': 'form-control phone-inputmask', 'required': False}),
            'celular': forms.NumberInput(attrs={'class': 'form-control phone-inputmask', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': False}),
            'nombres_contacto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'apellidos_contacto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'telefono_contacto': forms.NumberInput(attrs={'class': 'form-control phone-inputmask', 'required': False}),
            'celular_contacto': forms.NumberInput(attrs={'class': 'form-control phone-inputmask', 'required': True}),
            'email_contacto': forms.EmailInput(attrs={'class': 'form-control', 'required': False}),
            'grupo_etnico': forms.Select(attrs={'class': 'form-control', 'required': True}, choices=grupo_etnico_choices),
            'tipo_liderazgo': forms.Select(attrs={'class': 'form-control', 'required': True}, choices=tipo_liderazgo_choices),
            'organizacion_pertenece': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
        }
    #
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se dejan en blanco los campos dependientes de una selección previa de otro campo
        self.fields['usuario'].label = ""


class DenunciaLiderForm(forms.ModelForm):
    class Meta:
        model = DenunciaLider
        fields = ('usuario','departamento_denuncia', 'municipio_denuncia', 'situacion_riesgo', 'departamento_hecho', 'municipio_hecho', 'fecha_hecho',
              'medio', 'presunto_autor', 'descripcion', 'audio')
    #     exclude = ('valor',)
        tipo_doc_choices = [('CC','Cédula de ciudadania'), ('CE', 'Cédula de extranjeria'), ('PS', 'Pasaporte'), ('TI', 'Tarjeta de identidad')]
        sexo_choices = [('M','Masculino'), ('F', 'Femenino'), ('Otro', 'Otro'), ('No', 'No especificar')]
        grupo_etnico_choices = [('Afrocolombiano', 'Afrocolombiano'), ('Indigena', 'Indigena'), ('Negro', 'Negro'),
                            ('Palanquero', 'Palanquero'), ('Rom o Gitano', 'Rom o Gitano'), ('Sordo Raizal', 'Sordo Raizal')]
        tipo_liderazgo_choices = [('Activista político', 'Activista político'), ('Defensa derechos de la mujer', 'Defensa derechos de la mujer'),
                                  ('Defensa derechos comunidades afro', 'Defensa derechos comunidades afro'),
                                  ('Defensa derechos comunidades indígenas', 'Defensa derechos comunidades indígenas'),
                                  ('Defensa derechos campesinos', 'Defensa derechos campesinos'),
                                  ('Defensa derechos LGBTI', 'Defensa derechos LGBTI'), ('Líder reclamante', 'Líder reclamante'),
                                  ('Sindicato', 'Sindicato'), ('Otro', 'Otro')]

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'hidden': True}),
            #'tipo_doc': forms.Select(attrs={'class': 'form-control', 'required': True}, choices=tipo_doc_choices),
            'departamento_denuncia': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'municipio_denuncia': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'situacion_riesgo': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'departamento_hecho': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'municipio_hecho': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'fecha_hecho': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'medio': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'presunto_autor': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'required': True})
        }
    #
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se dejan en blanco los campos dependientes de una selección previa de otro campo
        self.fields['usuario'].label = ""
