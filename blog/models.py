from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=12)
    content = models.TextField()
    image = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
