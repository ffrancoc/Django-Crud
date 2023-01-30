from django.db import models
from datetime import datetime

GENRE_OPTIONS = (
    ('0', 'Masculino'),
    ('1', 'Femenino'),
    ('2', 'Otro')
)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField()
    birthday_date = models.DateField()
    genre = models.CharField(max_length=10, choices=GENRE_OPTIONS, default='0')
    create_at = models.DateTimeField(default=datetime.now(), null=False)

    def __str__(self):
        return f'Contacto creado con el nombre de {self.first_name} {self.last_name}'
