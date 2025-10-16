import django_filters
from .models import Medico, Paciente, ConsultaMedica, ESTADO_CHOICES,Especialidad

# ===============================
# FILTRO MEDICOS POR ESPECIALIDAD
# ===============================
class MedicoFilter(django_filters.FilterSet):
    especialidad = django_filters.ModelChoiceFilter(
        queryset=Especialidad.objects.all(),
        label="Especialidad"
    )

    class Meta:
        model = Medico
        fields = ['especialidad']

# ===============================
# FILTRO PACIENTES POR NOMBRE O MÉDICO
# ===============================
class PacienteFilter(django_filters.FilterSet):
    rut = django_filters.CharFilter(field_name='rut', lookup_expr='icontains', label='RUT del paciente')
    medico = django_filters.ModelChoiceFilter(
        queryset=Medico.objects.all(),
        field_name='consultas__medico',
        label='Médico',
        to_field_name='id'
    )

    class Meta:
        model = Paciente
        fields = ['rut', 'medico']

# ===============================
# FILTRO CONSULTAS POR PACIENTE, MÉDICO O ESTADO
# ===============================
class ConsultaFilter(django_filters.FilterSet):
    paciente = django_filters.ModelChoiceFilter(queryset=Paciente.objects.all())
    medico = django_filters.ModelChoiceFilter(queryset=Medico.objects.all())
    estado = django_filters.ChoiceFilter(choices=ESTADO_CHOICES)


    class Meta:
        model = ConsultaMedica
        fields = ['paciente', 'medico', 'estado']
