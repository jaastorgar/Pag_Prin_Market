from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_fecha_creacion(value):
    if value > timezone.now():
        raise ValidationError("La fecha de creacion no puede ser en el fututro.")


def validate_fecha_actualizacion(value):
    if value < timezone.datetime(2000, 1, 1, tzinfo=timezone.utc):
        raise ValidationError("La fecha de actualización no puede ser anterior al año 2000.")
