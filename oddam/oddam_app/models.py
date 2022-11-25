from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Institution(models.Model):
    INSTITUTION_TYPES = [
        (0, "fundacja"),
        (1, "organizacja_pozarzadowa"),
        (2, "zbiorka_lokalna"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    type = models.IntegerField(choices=INSTITUTION_TYPES, default=0)
    categories = models.ManyToManyField(Category, through='CategoryInstitution')

class CategoryInstitution(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, through='CategoryDonation')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=50)
    pick_up_date = models.DateTimeField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class CategoryDonation(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)


