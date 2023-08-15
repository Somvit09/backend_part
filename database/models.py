from django.db import models


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Hacks(models.Model):
    site = models.CharField(max_length=200)
    description = models.TextField()
    title = models.CharField(max_length=200)
    pwn_count = models.PositiveIntegerField()

    def __str__(self):
        return self.site


class HackMap(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    hack = models.ForeignKey(Hacks, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
