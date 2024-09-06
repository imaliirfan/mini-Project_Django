from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KL", "KIWI"),
        ("PL", "PLAIN"),
        ("EL", "ELACHI"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    data_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")

    ## in the admin panel you will get the object name as written in DB.
    def __str__(self):
        return self.name


# ONe TO MANy
## foreignKey


class ChaiReview(models.Model):
    chai = models.ForeignKey(
        ChaiVarity, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"


# MAny TO many
## directly from django models.ManyToManyField


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name="stores")

    def __str__(self):
        return self.name


# One to One
## directly from django models.OneToOneField


class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        ChaiVarity, on_delete=models.CASCADE, related_name="certificate"
    )
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.name.chai}"


# create the model with which we will be working with forms


class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.png", blank=True)

    def __str__(self):
        return self.title
