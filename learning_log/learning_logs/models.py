from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    text = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        "devolve uma representacao em string do modelo"
        return self.text
        

class Entry(models.Model):
    '''algo especifico sobre cada assunto'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''devolve uma representacao em string do modelo'''
        return self.text[:50] + '...'
    
    