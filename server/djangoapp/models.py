# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make
    
    def __str__(self):
        return self.name  # Return the name as the string representation of the object

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    CAR_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('wagon', 'Wagon'),
        # Add other types as needed
    ]
    
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='car_models')  # ForeignKey to CarMake
    dealer_id = models.IntegerField()  # The ID of the dealer
    name = models.CharField(max_length=100)  # Name of the car model
    car_type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)  # Type of the car (Sedan, SUV, etc.)
    year = models.DateField()  # Year of the car model
    
    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Return the car make and car model name
