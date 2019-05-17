from django.db import models

class Institucional(models.Model):
    image1 = models.ImageField('Imagem 1', upload_to='institute/', null=True)
    image2 = models.ImageField('Imagem 2', upload_to='institute/', null=True)
    image3 = models.ImageField('Imagem 3', upload_to='institute/', null=True)
    aboutInstitute = models.TextField('Sobre o CITi', max_length=520)

    class Meta:
        verbose_name = 'Sobre o Citi' 
        verbose_name_plural = 'Sobre o CITi'
# Create your models here.
