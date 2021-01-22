from django.db import models

# Create your models here.


choices = (
        ('private', 'Private'),
        ('bussines', 'bussines')

    )


class Adress(models.Model):
    town = models.CharField(max_length=250)
    street = models.CharField(max_length=50)
    home_number = models.CharField(max_length=50)
    flat_number = models.IntegerField(blank=True)
    post_code = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.street} {self.home_number}/{self.flat_number}'


class Person(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Phone(models.Model):

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    number = models.IntegerField()
    type = models.CharField(max_length=10, choices=choices)

    def __str__(self):
        return f'{self.number} - {self.type}'

class Email(models.Model):
    email_adress = models.EmailField()
    type = models.CharField(max_length=10, choices=choices)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=40)
    person = models.ManyToManyField(Person)