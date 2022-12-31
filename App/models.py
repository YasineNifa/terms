from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    terms = models.BooleanField("Accepted the terms", default=False)

    def __str__(self):
        return self.name