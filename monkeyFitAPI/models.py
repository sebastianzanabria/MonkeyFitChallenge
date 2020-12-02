from django.db import models

class Place(models.Model):
    place_id = models.CharField(max_length=200) 
    name = models.CharField(max_length=200, null=True) 
    formatted_address = models.CharField(max_length=200, null=True)
    business_status = models.CharField(max_length=200, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    url = models.CharField(max_length=200, null=True)
    user_ratings_total = models.IntegerField(null=True)
    utc_offset = models.IntegerField(null=True)
