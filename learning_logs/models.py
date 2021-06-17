from django.db import models
from django.contrib.auth.models import User  # importo el model User que tiene django
# Create your models here.


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)  # You use CharField when you want to store a small amount of text
    date_added = models.DateTimeField(auto_now_add=True)  # cuando se crea el Topic automaticamente se llena este campo con la fecha y hora actual
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # aca designo una relacion del topic con un user, si se borra el user se borra el topic

    def __str__(self):
        """Return a string representation of the model"""
        return self.text  # Django calls a __str__() method to display a simple representation of a model


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # primero dice que el topic es un objeto Topic y on_delete sirve para
    text = models.TextField()    # indicar que hacer si se borra el objeto referenciado (que hacer con los entries si se borra el Topic)
    date_added = models.DateTimeField(auto_now_add=True)  # models.CASCADE hace que si se borra un topic se borren todas sus entries.
                                                    # es algo de SQL (no de Django). En internet (stackoverflow) se pueden ver otras opciones

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of a model"""
        if len(self.text) > 50:
            frase = self.text[:50] + "..."
        else:
            frase = self.text
        return frase
