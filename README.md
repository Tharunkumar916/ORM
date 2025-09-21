# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

<img width="1028" height="677" alt="Screenshot 2025-09-21 195823" src="https://github.com/user-attachments/assets/7cd8adb3-71cf-4c17-b732-50530fe59695" />


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

model.py:
```
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=40)
    year = models.DateField()
    price = models.IntegerField()
    type = models.CharField(max_length=10)

```

admin.py:
```
from django.contrib import admin
from . models import Car
# Register your models here.

admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    list_display = ('id','brand','model','year','price','type')
```


## OUTPUT

Include the screenshot of your admin page.
<img width="1031" height="520" alt="Screenshot 2025-09-21 195945" src="https://github.com/user-attachments/assets/ec8545c4-9e47-4743-9baa-f649792fcf6c" />



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
