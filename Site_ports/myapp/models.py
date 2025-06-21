from django.db import models

# Create your models here.

class Myapp_Model(models.Model):
    title = models.CharField(max_length=200) # Заголовок
    description = models.TextField() # Описание
    image = models.ImageField(upload_to='images/') # Путь для загрузки изображения

    def __str__(self): # Обратите внимание: __str__, а не str
        return self.title
