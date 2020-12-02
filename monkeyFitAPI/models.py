from django.db import models

class Place(models.Model):
    place_id = models.CharField(max_length=40) 
    name = models.CharField(max_length=30, null=True) 
    formatted_address = models.CharField(max_length=100, null=True)
    business_status = models.CharField(max_length=30, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    url = models.CharField(max_length=100, null=True)
    user_ratings_total = models.IntegerField(null=True)
    utc_offset = models.IntegerField(null=True)
