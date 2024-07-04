from django.db import models
from django.forms import ModelForm
# Create your models here.

class Todo(models.Model):
    text=models.CharField( max_length=1200,blank=False,null=False)
    date=models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.text
    
class TodoForm(ModelForm):
    class Meta:
        model=Todo
        fields=['text',]