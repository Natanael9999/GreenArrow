from django.db import models

# Create your models here.

class Heroes(models.Model):
    name = models.CharField(max_length=200)
    pseudonym = models.CharField(max_length=200)
    motivation = models.CharField(max_length=200)
    age = models.IntegerField(max_length=4)

    def __str__(self):
        return self.name

class Villain(models.Model):
    name = models.CharField(max_length=200)
    pseudonym = models.CharField(max_length=200)
    motivation = models.CharField(max_length=200)
    age = models.IntegerField(max_length=4)
    defeat = models.ForeignKey(Heroes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Places(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name