from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo', help_text="Ingrese el Titulo")
    description = models.TextField(verbose_name='Descripcion', help_text="Ingrese el Contenido")
    image = models.ImageField(upload_to='proyectos', verbose_name='Imagen', help_text="Ingrese la imagen")
    link = models.URLField(null=True, blank=True, verbose_name='Dirección Web')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(auto_now=True, verbose_name='Editado el')
    
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return f"{self.title}"