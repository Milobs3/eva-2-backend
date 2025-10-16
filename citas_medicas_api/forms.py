from django import forms
from .models import (
    Especialidad, Paciente, Medico, ConsultaMedica,
    Tratamiento, Medicamento, RecetaMedica, HistorialMedico 
)

# =======================================================
# FORMULARIOS PARA CADA ENTIDAD
# =======================================================

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

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

class RecetaMedicaForm(forms.ModelForm):
    class Meta:
        model = RecetaMedica
        fields = '__all__'
        
class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = '__all__'
