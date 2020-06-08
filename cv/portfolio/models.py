from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=140, verbose_name="Titulo") # titulo con largo máximo
    description = models.TextField(verbose_name="Descripción") # texto sin largo definido
    image = models.ImageField(verbose_name="Imagen", upload_to="projects") # imagen
    created = models.DateTimeField(auto_now_add=True) # fecha de creacion 
    updated = models.DateTimeField(auto_now=True) # fecha de modificacion

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
    def __str__(self):
        return self.title