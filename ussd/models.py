from django.db import models

# Create your models here.
class Question (models.Model): 
    phone_number = models.CharField(max_length=20)
    question_text = models.TextField()
    ai_responce = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__ (self):
    return f"{self.phone_number} - {self.question_text[:30]}"