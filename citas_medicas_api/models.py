from django.db import models
from django.utils import timezone

# ===============================
# ESPECIALIDAD
# ===============================
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nombre

# ===============================
# PACIENTE
# ===============================
TIPO_SANGRE_CHOICES = [
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
]

class Paciente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    rut = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    tipo_sangre = models.CharField(max_length=3, choices=TIPO_SANGRE_CHOICES, blank=True)
    activo = models.BooleanField(default=True)
    direccion = models.TextField(blank=True)

    class Meta:
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ===============================
# SEGURO MEDICO (nueva tabla)
# ===============================
class SeguroMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='seguros')
    nombre = models.CharField(max_length=150)
    poliza = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.poliza} ({self.paciente})"

# ===============================
# MEDICO
# ===============================
class Medico(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    rut = models.CharField(max_length=12, default="00000000-0")
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, related_name='medicos')
    matricula = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=30, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr(a). {self.nombre} {self.apellido} ({self.especialidad})"

# ===============================
# TRATAMIENTO
# ===============================
class Tratamiento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    duracion_dias = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre

# ===============================
# MEDICAMENTO
# ===============================
class Medicamento(models.Model):
    nombre = models.CharField(max_length=200)
    laboratorio = models.CharField(max_length=100, blank=True)
    stock = models.PositiveIntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nombre

# ===============================
# CONSULTA MEDICA
# ===============================
ESTADO_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('FINALIZADA', 'Finalizada'),
    ('CANCELADA', 'Cancelada'),
]

class ConsultaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, related_name='consultas')
    fecha_consulta = models.DateTimeField(default=timezone.now)
    motivo = models.CharField(max_length=250)
    diagnostico = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    tratamientos = models.ManyToManyField(Tratamiento, blank=True, related_name='consultas')

    def __str__(self):
        return f"Consulta {self.id} - {self.paciente} - {self.fecha_consulta.date()}"

# ===============================
# RECETA MEDICA
# ===============================
class RecetaMedica(models.Model):
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE, default=1)
    observaciones = models.TextField(blank=True)
    medicamentos = models.ManyToManyField(Medicamento, through='RecetaMedicamento')

    def __str__(self):
        return f"Receta {self.id} - {self.consulta.paciente}"

# ===============================
# RECETA MEDICAMENTO
# ===============================
class RecetaMedicamento(models.Model):
    receta = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dosis = models.CharField(max_length=100, blank=True)
    frecuencia = models.CharField(max_length=100, blank=True)
    duracion = models.CharField(max_length=100, blank=True)

# ===============================
# Historial medico
# ===============================
class HistorialMedico(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='historiales')
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE, related_name='historiales')
    consulta = models.ForeignKey('ConsultaMedica', on_delete=models.CASCADE, related_name='historiales')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Historial Médico'
        verbose_name_plural = 'Historiales Médicos'

    def __str__(self):
        return f"Historial {self.id} - {self.paciente.nombre} con {self.medico.nombre}"