from django.db import models

# Create your models here.

class Ticket(models.Model):
    owner = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    number = models.SmallIntegerField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.owner} - {self.number}'
