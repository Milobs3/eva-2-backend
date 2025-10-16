from django import forms
from django.core.exceptions import ValidationError
from .models import (
    Especialidad, Paciente, Medico, ConsultaMedica,
    Tratamiento, Medicamento, RecetaMedica, HistorialMedico, SeguroMedico
)
import re

# ===============================
# VALIDADORES REUTILIZABLES
# ===============================

def validar_rut(value):
    """Valida formato RUT chileno"""
    rut_regex = re.compile(r'^\d{7,8}-[0-9kK]$')
    if not rut_regex.match(value):
        raise ValidationError('RUT inválido. Formato esperado: 12345678-9')

def validar_email(value):
    email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    if not email_regex.match(value):
        raise ValidationError('Correo electrónico inválido')

def validar_texto_sin_numeros(value, campo='Campo'):
    if any(char.isdigit() for char in value):
        raise ValidationError(f'{campo} no puede contener números')


# ===============================
# FORMULARIOS
# ===============================

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    rut = forms.CharField(validators=[validar_rut])
    email = forms.EmailField(validators=[validar_email])

    class Meta:
        model = Paciente
        fields = '__all__'

    def clean_nombre(self):
        validar_texto_sin_numeros(self.cleaned_data['nombre'], 'Nombre')
        return self.cleaned_data['nombre']

    def clean_apellido(self):
        validar_texto_sin_numeros(self.cleaned_data['apellido'], 'Apellido')
        return self.cleaned_data['apellido']

class MedicoForm(forms.ModelForm):
    email = forms.EmailField(validators=[validar_email])

    class Meta:
        model = Medico
        fields = '__all__'

    def clean_nombre(self):
        validar_texto_sin_numeros(self.cleaned_data['nombre'], 'Nombre')
        return self.cleaned_data['nombre']

    def clean_apellido(self):
        validar_texto_sin_numeros(self.cleaned_data['apellido'], 'Apellido')
        return self.cleaned_data['apellido']

class ConsultaMedicaForm(forms.ModelForm):
    class Meta:
        model = ConsultaMedica
        fields = '__all__'

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise ValidationError('El stock no puede ser negativo')
        return stock

    def clean_precio_unitario(self):
        precio = self.cleaned_data['precio_unitario']
        if precio < 0:
            raise ValidationError('El precio no puede ser negativo')
        return precio

class RecetaMedicaForm(forms.ModelForm):
    class Meta:
        model = RecetaMedica
        fields = '__all__'

class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = '__all__'

class SeguroMedicoForm(forms.ModelForm):
    class Meta:
        model = SeguroMedico
        fields = '__all__'
