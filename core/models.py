from django.db import models

# Create your models here.


class Elder(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="Anciano gobernante")
    photo = models.ImageField(upload_to="elders/")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order"]
