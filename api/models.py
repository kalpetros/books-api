from django.core.validators import RegexValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):
    name = models.CharField(max_length=250, unique=True)
    telephone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Format should be: '+999999999'. Up to 15 digits allowed.")
    telephone = models.CharField(
        validators=[telephone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)
    publisher = models.ForeignKey(
        Publisher,
        related_name='books',
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    isbn = models.CharField(
        unique=True,
        max_length=13,
        validators=[
            RegexValidator(
                regex='^([0-9]{10}|[0-9]{13})$',
                message="ISBN should be 10 or 13 digits.")
        ])
    created = models.DateField()
    VISIBILITY_STATUS_CHOICES = [
        ('AC', 'Active'),
        ('IN', 'Inactive'),
    ]
    visibility_status = models.CharField(
        max_length=2, choices=VISIBILITY_STATUS_CHOICES, default='AC')

    def __str__(self):
        return self.title
