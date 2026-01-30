from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DT", "Draft"
        Published = "PB" , "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    img = models.ImageField(upload_to='new/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(timezone.now)
    status = models.CharField(max_length=2 , choices=Status.choices , default=Status.Draft)

    class Meta:
        ordering = ["-published_at"]
    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.name

img = models.ImageField(upload_to='new/images/')