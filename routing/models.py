from django.db import models

# Create your models here


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle = models.CharField(max_length=100)
    current_location = models.CharField(max_length=255, null=True)


class Route(models.Model):
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    waypoints = models.TextField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    optimized_route = models.TextField(null=True)
