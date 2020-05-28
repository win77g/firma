from django.db import models

# Create your models here.
class Message(models.Model):
      name = models.CharField(max_length=100,blank=True, null=True, default=None)
      email = models.CharField(max_length=200,blank=True, null=True, default=None)
      phone = models.CharField(max_length=200,blank=True, null=True, default=None)
      message = models.TextField(max_length=200,blank=True, null=True, default=None)
      # control = models.BooleanField(default=False)
# вывод одного поля
      def __str__(self):
          return "Сообщения "
      class Meta:
          verbose_name = 'Сообщение'
          verbose_name_plural = 'Сообщения'
