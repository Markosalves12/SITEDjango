from django.db import models

PRIORITY = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=60)
    question = models.TextField(max_length=400)
    priority = models.CharField(max_length=10, choices=PRIORITY)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "The question"
        verbose_name_plural = "People Questions"