from django.db import models

# Create your models here.
class Contact(models.Model):
    #name=models.CharFiels(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)
    #subject=models.TextField()

    def __str__(self):
        return self.email

class dead(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    #password=models.CharField(max_length=200)
    #subject=models.TextField()
    phoneNumber=models.CharField(max_length=10)
    Address=models.TextField()
    about=models.TextField()

    def __str__(self):
        return self.email

class harassement(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    # password=models.CharField(max_length=200)
    # subject=models.TextField()
    phoneNumber = models.CharField(max_length=10)
    Address = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.email

class injured(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    # password=models.CharField(max_length=200)
    # subject=models.TextField()
    phoneNumber = models.CharField(max_length=10)
    Address = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.email

class Feedback(models.Model):
    about=models.CharField(max_length=300)

    def __str__(self):
        return self.about


