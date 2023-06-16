from django.core.exceptions import ValidationError
import django.db import models
from django.utils import timezone


class Productos(models.Model):

    def clean(self):
        if self.fechaActualizacion <= self.fechaCreacion:
            raise ValidationError("La fecha de actualizacion debe ser posterior a la fecha de creacion.")


    def clean_fields(self, exclude=None):
        
        super().clean_fields(exclude=exclude)

        current_date = timezone.now().date()
        if self.fechaCreacion.date() != current_date:
            raise ValidationError("La fecha de creacion debe ser la fecha actual.")


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)