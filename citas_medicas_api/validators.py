
import re
from django.core.exceptions import ValidationError

def validar_rut(value):
    """Valida el RUT chileno (formato y dígito verificador)"""
    rut_regex = re.compile(r'^\d{7,8}-[0-9kK]$')
    if not rut_regex.match(value):
        raise ValidationError('RUT inválido. Formato esperado: 12345678-9')


def validar_email(value):
    """Valida el correo electrónico"""
    email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    if not email_regex.match(value):
        raise ValidationError('Correo electrónico inválido')

def validar_texto_sin_numeros(value, campo='Este campo'):
    """Valida que un texto no contenga números"""
    if any(char.isdigit() for char in value):
        raise ValidationError(f'{campo} no puede contener números')
