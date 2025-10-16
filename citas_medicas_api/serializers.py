from rest_framework import serializers
from .models import (Especialidad, Paciente, HistorialMedico, Medico,
                     Tratamiento, Medicamento, RecetaMedica, RecetaMedicamento, ConsultaMedica)

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'


class PacienteSerializer(serializers.ModelSerializer):
    historiales = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'apellido', 'rut', 'fecha_nacimiento', 'telefono', 'email', 'tipo_sangre', 'historiales']


class HistorialMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialMedico
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    especialidad = EspecialidadSerializer(read_only=True)
    especialidad_id = serializers.PrimaryKeyRelatedField(queryset=Especialidad.objects.all(), source='especialidad', write_only=True)

    class Meta:
        model = Medico
        fields = ['id', 'nombre', 'apellido', 'matricula', 'telefono', 'especialidad', 'especialidad_id']


class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'


class RecetaMedicamentoSerializer(serializers.ModelSerializer):
    medicamento = MedicamentoSerializer(read_only=True)
    medicamento_id = serializers.PrimaryKeyRelatedField(queryset=Medicamento.objects.all(), source='medicamento', write_only=True)

    class Meta:
        model = RecetaMedicamento
        fields = ['id', 'receta', 'medicamento', 'medicamento_id', 'dosis', 'frecuencia']


class RecetaMedicaSerializer(serializers.ModelSerializer):
    medicamentos_detalle = RecetaMedicamentoSerializer(source='recetamedicamento_set', many=True, read_only=True)

    class Meta:
        model = RecetaMedica
        fields = ['id', 'paciente', 'medico', 'fecha', 'observaciones', 'medicamentos_detalle']


class ConsultaMedicaSerializer(serializers.ModelSerializer):
    tratamientos = TratamientoSerializer(many=True, read_only=True)
    tratamientos_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Tratamiento.objects.all(), write_only=True, source='tratamientos')

    class Meta:
        model = ConsultaMedica
        fields = ['id', 'paciente', 'medico', 'fecha', 'motivo', 'diagnostico', 'tratamientos', 'tratamientos_ids', 'receta']
