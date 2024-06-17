from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class RaingouProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    techonolies_use = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    
class RaingouSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name 