from django.db import models

# Smart Campus Navigation
class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

# Lost & Found
class LostItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_lost = models.DateField()
    contact_info = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.name

class FoundItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_found = models.DateField()
    contact_info = models.CharField(max_length=255)


    def __str__(self):
        return self.name

# Career Portal
class JobListing(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
