# citas_medicas_api/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .filters import MedicoFilter, PacienteFilter, ConsultaFilter
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica,HistorialMedico,SeguroMedico
from .forms import (
    EspecialidadForm, PacienteForm, MedicoForm, ConsultaMedicaForm,
    TratamientoForm, MedicamentoForm, RecetaMedicaForm,HistorialMedicoForm,SeguroMedicoForm
)

# =======================================================
# HOME PAGE
# =======================================================
def home(request):
    return render(request, 'citas_medicas_api/home.html')


# =======================================================
# CRUD Especialidad
# =======================================================
class EspecialidadListView(View):
    def get(self, request):
        especialidades = Especialidad.objects.all()
        return render(request, 'citas_medicas_api/especialidad/list.html', {'especialidades': especialidades})

class EspecialidadCreateView(View):
    def get(self, request):
        form = EspecialidadForm()
        return render(request, 'citas_medicas_api/especialidad/create.html', {'form': form})

    def post(self, request):
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('especialidad-list')
        return render(request, 'citas_medicas_api/especialidad/create.html', {'form': form})

class EspecialidadUpdateView(View):
    def get(self, request, pk):
        especialidad = get_object_or_404(Especialidad, pk=pk)
        form = EspecialidadForm(instance=especialidad)
        return render(request, 'citas_medicas_api/especialidad/update.html', {'form': form})

    def post(self, request, pk):
        especialidad = get_object_or_404(Especialidad, pk=pk)
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('especialidad-list')
        return render(request, 'citas_medicas_api/especialidad/update.html', {'form': form})

class EspecialidadDeleteView(View):
    def get(self, request, pk):
        especialidad = get_object_or_404(Especialidad, pk=pk)
        return render(request, 'citas_medicas_api/especialidad/delete.html', {'especialidad': especialidad})

    def post(self, request, pk):
        especialidad = get_object_or_404(Especialidad, pk=pk)
        especialidad.delete()
        return redirect('especialidad-list')


# =======================================================
# CRUD Paciente
# =======================================================

class PacienteListView(ListView):
    model = Paciente
    template_name = 'citas_medicas_api/paciente/list.html'
    context_object_name = 'pacientes'

    def get_queryset(self):
        queryset = super().get_queryset()
        rut = self.request.GET.get('rut')
        if rut:
            queryset = queryset.filter(rut__icontains=rut)
        return queryset

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'citas_medicas_api/paciente/create.html'
    success_url = '/pacientes/'

    def post(self, request):
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente-list')
        return render(request, self.template_name, {'form': form})

class PacienteUpdateView(View):
    def get(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(instance=paciente)
        return render(request, 'citas_medicas_api/paciente/update.html', {'form': form})

    def post(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente-list')
        return render(request, 'citas_medicas_api/paciente/update.html', {'form': form})

class PacienteDeleteView(View):
    def get(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        return render(request, 'citas_medicas_api/paciente/delete.html', {'paciente': paciente})

    def post(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        paciente.delete()
        return redirect('paciente-list')


# =======================================================
# CRUD Medico
# =======================================================

class MedicoListView(View):
    def get(self, request):
        f = MedicoFilter(request.GET, queryset=Medico.objects.all())
        medicos = f.qs
        return render(request, 'citas_medicas_api/medico/list.html', {'medicos': medicos, 'filter': f})

class MedicoCreateView(View):
    def get(self, request):
        form = MedicoForm()
        return render(request, 'citas_medicas_api/medico/create.html', {'form': form})

    def post(self, request):
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medico-list')
        return render(request, 'citas_medicas_api/medico/create.html', {'form': form})

class MedicoUpdateView(View):
    def get(self, request, pk):
        medico = get_object_or_404(Medico, pk=pk)
        form = MedicoForm(instance=medico)
        return render(request, 'citas_medicas_api/medico/update.html', {'form': form})

    def post(self, request, pk):
        medico = get_object_or_404(Medico, pk=pk)
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medico-list')
        return render(request, 'citas_medicas_api/medico/update.html', {'form': form})

class MedicoDeleteView(View):
    def get(self, request, pk):
        medico = get_object_or_404(Medico, pk=pk)
        return render(request, 'citas_medicas_api/medico/delete.html', {'medico': medico})

    def post(self, request, pk):
        medico = get_object_or_404(Medico, pk=pk)
        medico.delete()
        return redirect('medico-list')


# =======================================================
# CRUD ConsultaMedica
# =======================================================
class ConsultaListView(View):
    def get(self, request):
        consultas = ConsultaMedica.objects.all()
        filtro = ConsultaFilter(request.GET, queryset=consultas)
        return render(request, 'citas_medicas_api/consulta_medica/list.html', {'filter': filtro, 'consultas': filtro.qs})


from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import ConsultaMedica
from .forms import ConsultaMedicaForm

class ConsultaCreateView(CreateView):
    model = ConsultaMedica
    form_class = ConsultaMedicaForm
    template_name = 'citas_medicas_api/consulta_medica/create.html'
    
    # Redirigir al listado al guardar
    def get_success_url(self):
        # Si querés mantener el filtro en la URL, podés hacer algo como:
        rut = self.request.GET.get('rut', '')
        if rut:
            return reverse_lazy('consulta-list') + f'?rut={rut}'
        return reverse_lazy('consulta-list')


class ConsultaUpdateView(View):
    def get(self, request, pk):
        consulta = get_object_or_404(ConsultaMedica, pk=pk)
        form = ConsultaMedicaForm(instance=consulta)
        return render(request, 'citas_medicas_api/consulta_medica/update.html', {'form': form})

    def post(self, request, pk):
        consulta = get_object_or_404(ConsultaMedica, pk=pk)
        form = ConsultaMedicaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta-list')
        return render(request, 'citas_medicas_api/consulta_medica/update.html', {'form': form})

class ConsultaDeleteView(View):
    def get(self, request, pk):
        consulta = get_object_or_404(ConsultaMedica, pk=pk)
        return render(request, 'citas_medicas_api/consulta_medica/delete.html', {'consulta': consulta})

    def post(self, request, pk):
        consulta = get_object_or_404(ConsultaMedica, pk=pk)
        consulta.delete()
        return redirect('consulta-list')


# =======================================================
# CRUD Tratamiento
# =======================================================
class TratamientoListView(View):
    def get(self, request):
        tratamientos = Tratamiento.objects.all()
        return render(request, 'citas_medicas_api/tratamiento/list.html', {'tratamientos': tratamientos})

class TratamientoCreateView(View):
    def get(self, request):
        form = TratamientoForm()
        return render(request, 'citas_medicas_api/tratamiento/create.html', {'form': form})

    def post(self, request):
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tratamiento-list')
        return render(request, 'citas_medicas_api/tratamiento/create.html', {'form': form})

class TratamientoUpdateView(View):
    def get(self, request, pk):
        tratamiento = get_object_or_404(Tratamiento, pk=pk)
        form = TratamientoForm(instance=tratamiento)
        return render(request, 'citas_medicas_api/tratamiento/update.html', {'form': form})

    def post(self, request, pk):
        tratamiento = get_object_or_404(Tratamiento, pk=pk)
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return redirect('tratamiento-list')
        return render(request, 'citas_medicas_api/tratamiento/update.html', {'form': form})

class TratamientoDeleteView(View):
    def get(self, request, pk):
        tratamiento = get_object_or_404(Tratamiento, pk=pk)
        return render(request, 'citas_medicas_api/tratamiento/delete.html', {'tratamiento': tratamiento})

    def post(self, request, pk):
        tratamiento = get_object_or_404(Tratamiento, pk=pk)
        tratamiento.delete()
        return redirect('tratamiento-list')


# =======================================================
# CRUD Medicamento
# =======================================================
class MedicamentoListView(View):
    def get(self, request):
        medicamentos = Medicamento.objects.all()
        return render(request, 'citas_medicas_api/medicamento/list.html', {'medicamentos': medicamentos})

class MedicamentoCreateView(View):
    def get(self, request):
        form = MedicamentoForm()
        return render(request, 'citas_medicas_api/medicamento/create.html', {'form': form})

    def post(self, request):
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamento-list')
        return render(request, 'citas_medicas_api/medicamento/create.html', {'form': form})

class MedicamentoUpdateView(View):
    def get(self, request, pk):
        medicamento = get_object_or_404(Medicamento, pk=pk)
        form = MedicamentoForm(instance=medicamento)
        return render(request, 'citas_medicas_api/medicamento/update.html', {'form': form})

    def post(self, request, pk):
        medicamento = get_object_or_404(Medicamento, pk=pk)
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('medicamento-list')
        return render(request, 'citas_medicas_api/medicamento/update.html', {'form': form})

class MedicamentoDeleteView(View):
    def get(self, request, pk):
        medicamento = get_object_or_404(Medicamento, pk=pk)
        return render(request, 'citas_medicas_api/medicamento/delete.html', {'medicamento': medicamento})

    def post(self, request, pk):
        medicamento = get_object_or_404(Medicamento, pk=pk)
        medicamento.delete()
        return redirect('medicamento-list')


# =======================================================
# CRUD RecetaMedica
# =======================================================
class RecetaListView(View):
    def get(self, request):
        recetas = RecetaMedica.objects.all()
        return render(request, 'citas_medicas_api/receta_medica/list.html', {'recetas': recetas})

class RecetaCreateView(View):
    def get(self, request):
        form = RecetaMedicaForm()
        return render(request, 'citas_medicas_api/receta_medica/create.html', {'form': form})

    def post(self, request):
        form = RecetaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receta-list')
        return render(request, 'citas_medicas_api/receta_medica/create.html', {'form': form})

class RecetaUpdateView(View):
    def get(self, request, pk):
        receta = get_object_or_404(RecetaMedica, pk=pk)
        form = RecetaMedicaForm(instance=receta)
        return render(request, 'citas_medicas_api/receta_medica/update.html', {'form': form})

    def post(self, request, pk):
        receta = get_object_or_404(RecetaMedica, pk=pk)
        form = RecetaMedicaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('receta-list')
        return render(request, 'citas_medicas_api/receta_medica/update.html', {'form': form})

class RecetaDeleteView(View):
    def get(self, request, pk):
        receta = get_object_or_404(RecetaMedica, pk=pk)
        return render(request, 'citas_medicas_api/receta_medica/delete.html', {'receta': receta})

    def post(self, request, pk):
        receta = get_object_or_404(RecetaMedica, pk=pk)
        receta.delete()
        return redirect('receta-list')
    
   # =======================================================
# CRUD HistorialMedico
# =======================================================
class HistorialListView(View):
    def get(self, request):
        historiales = HistorialMedico.objects.all()
        return render(request, 'citas_medicas_api/historial/list.html', {'historiales': historiales})

class HistorialCreateView(CreateView):
    model = HistorialMedico
    form_class = HistorialMedicoForm
    template_name = 'citas_medicas_api/historial/create.html'
    success_url = '/historiales/'

class HistorialUpdateView(View):
    def get(self, request, pk):
        historial = get_object_or_404(HistorialMedico, pk=pk)
        form = HistorialMedico(instance=historial)
        return render(request, 'citas_medicas_api/historial/update.html', {'form': form})

    def post(self, request, pk):
        historial = get_object_or_404(HistorialMedico, pk=pk)
        form = HistorialMedico(request.POST, instance=historial)
        if form.is_valid():
            form.save()
            return redirect('historial-list')
        return render(request, 'citas_medicas_api/historial/update.html', {'form': form})

class HistorialDeleteView(View):
    def get(self, request, pk):
        historial = get_object_or_404(HistorialMedico, pk=pk)
        return render(request, 'citas_medicas_api/historial/delete.html', {'historial': historial})

    def post(self, request, pk):
        historial = get_object_or_404(HistorialMedico, pk=pk)
        historial.delete()
        return redirect('historial-list')

# =======================================================
# CRUD SeguroMedico
# =======================================================
class SeguroMedicoListView(View):
    def get(self, request):
        seguros = SeguroMedico.objects.all()
        return render(request, 'citas_medicas_api/seguro_medico/list.html', {'seguros': seguros})

class SeguroMedicoCreateView(CreateView):
    model = SeguroMedico
    form_class = SeguroMedicoForm
    template_name = 'citas_medicas_api/seguro_medico/create.html'
    success_url = '/seguros/'  # ruta a la lista de seguros

class SeguroMedicoUpdateView(View):
    def get(self, request, pk):
        seguro = get_object_or_404(SeguroMedico, pk=pk)
        form = SeguroMedico(instance=seguro)
        return render(request, 'citas_medicas_api/seguro_medico/update.html', {'form': form})

    def post(self, request, pk):
        seguro = get_object_or_404(SeguroMedico, pk=pk)
        form = SeguroMedico(request.POST, instance=seguro)
        if form.is_valid():
            form.save()
            return redirect('seguro-list')
        return render(request, 'citas_medicas_api/seguro_medico/update.html', {'form': form})

class SeguroMedicoDeleteView(View):
    def get(self, request, pk):
        seguro = get_object_or_404(SeguroMedico, pk=pk)
        return render(request, 'citas_medicas_api/seguro_medico/delete.html', {'seguro': seguro})

    def post(self, request, pk):
        seguro = get_object_or_404(SeguroMedico, pk=pk)
        seguro.delete()
        return redirect('seguro-list')
