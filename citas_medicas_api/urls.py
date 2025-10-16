from django.urls import path
from . import views
from .views import (
    HistorialListView,
    HistorialCreateView,
    HistorialUpdateView,
    HistorialDeleteView,
)
urlpatterns = [
    # =============================
    # HOME
    # =============================
    path('', views.home, name='home'),

    # =============================
    # ESPECIALIDADES
    # =============================
    path('especialidades/', views.EspecialidadListView.as_view(), name='especialidad-list'),
    path('especialidades/create/', views.EspecialidadCreateView.as_view(), name='especialidad-create'),
    path('especialidades/<int:pk>/update/', views.EspecialidadUpdateView.as_view(), name='especialidad-update'),
    path('especialidades/<int:pk>/delete/', views.EspecialidadDeleteView.as_view(), name='especialidad-delete'),

    # =============================
    # PACIENTES
    # =============================
    path('pacientes/', views.PacienteListView.as_view(), name='paciente-list'),
    path('pacientes/create/', views.PacienteCreateView.as_view(), name='paciente-create'),
    path('pacientes/<int:pk>/update/', views.PacienteUpdateView.as_view(), name='paciente-update'),
    path('pacientes/<int:pk>/delete/', views.PacienteDeleteView.as_view(), name='paciente-delete'),

    # =============================
    # MEDICOS
    # =============================
    path('medicos/', views.MedicoListView.as_view(), name='medico-list'),
    path('medicos/create/', views.MedicoCreateView.as_view(), name='medico-create'),
    path('medicos/<int:pk>/update/', views.MedicoUpdateView.as_view(), name='medico-update'),
    path('medicos/<int:pk>/delete/', views.MedicoDeleteView.as_view(), name='medico-delete'),

    # =============================
    # CONSULTAS MEDICAS
    # =============================
    path('consultas/', views.ConsultaListView.as_view(), name='consulta-list'),
    path('consultas/create/', views.ConsultaCreateView.as_view(), name='consulta-create'),
    path('consultas/<int:pk>/update/', views.ConsultaUpdateView.as_view(), name='consulta-update'),
    path('consultas/<int:pk>/delete/', views.ConsultaDeleteView.as_view(), name='consulta-delete'),

    # =============================
    # TRATAMIENTOS
    # =============================
    path('tratamientos/', views.TratamientoListView.as_view(), name='tratamiento-list'),
    path('tratamientos/create/', views.TratamientoCreateView.as_view(), name='tratamiento-create'),
    path('tratamientos/<int:pk>/update/', views.TratamientoUpdateView.as_view(), name='tratamiento-update'),
    path('tratamientos/<int:pk>/delete/', views.TratamientoDeleteView.as_view(), name='tratamiento-delete'),

    # =============================
    # MEDICAMENTOS
    # =============================
    path('medicamentos/', views.MedicamentoListView.as_view(), name='medicamento-list'),
    path('medicamentos/create/', views.MedicamentoCreateView.as_view(), name='medicamento-create'),
    path('medicamentos/<int:pk>/update/', views.MedicamentoUpdateView.as_view(), name='medicamento-update'),
    path('medicamentos/<int:pk>/delete/', views.MedicamentoDeleteView.as_view(), name='medicamento-delete'),

    # =============================
    # RECETAS MEDICAS
    # =============================
    path('recetas/', views.RecetaListView.as_view(), name='receta-list'),
    path('recetas/create/', views.RecetaCreateView.as_view(), name='receta-create'),
    path('recetas/<int:pk>/update/', views.RecetaUpdateView.as_view(), name='receta-update'),
    path('recetas/<int:pk>/delete/', views.RecetaDeleteView.as_view(), name='receta-delete'),

   # =============================
    # HISTORIALES MEDICOS
    # =============================
     path('historiales/', HistorialListView.as_view(), name='historial-list'),
    path('historiales/crear/', HistorialCreateView.as_view(), name='historial-create'),
    path('historiales/editar/<int:pk>/', HistorialUpdateView.as_view(), name='historial-update'),
    path('historiales/eliminar/<int:pk>/', HistorialDeleteView.as_view(), name='historial-delete'),
    
    # =============================
    # SEGUROS MEDICOS
    # =============================
    path('seguros/', views.SeguroMedicoListView.as_view(), name='seguro-list'),
    path('seguros/create/', views.SeguroMedicoCreateView.as_view(), name='seguro-create'),
    path('seguros/<int:pk>/update/', views.SeguroMedicoUpdateView.as_view(), name='seguro-update'),
    path('seguros/<int:pk>/delete/', views.SeguroMedicoDeleteView.as_view(), name='seguro-delete'),

]