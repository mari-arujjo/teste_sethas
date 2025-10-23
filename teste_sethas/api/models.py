from django.db import models

class Consumidor(models.Model):
    user = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    is_isento = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
