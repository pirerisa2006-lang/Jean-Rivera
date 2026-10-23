from django.db import models

# Create your models here.
#Nombre del modelo con mayuscula
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name="description")
    img = models.ImageField(upload_to='images/',verbose_name='Imagen')
    link = models.URLField(verbose_name='Enlace',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de edicion')
    class Meta:
        ordering = ('title',)
        db_table = 'projects'
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    def _str_(self):
        return self.title