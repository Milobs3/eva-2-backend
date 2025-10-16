from django.contrib import admin
from .models import (Especialidad, Paciente, Medico,
                     Tratamiento, Medicamento, RecetaMedica, RecetaMedicamento, ConsultaMedica)

admin.site.register(Especialidad)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Tratamiento)
admin.site.register(Medicamento)
admin.site.register(RecetaMedica)
admin.site.register(RecetaMedicamento)
admin.site.register(ConsultaMedica)
