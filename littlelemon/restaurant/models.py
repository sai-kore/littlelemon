from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    inventory = models.IntegerField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.title