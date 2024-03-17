from django.db import models



class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    weekly_update = models.BooleanField(default=False)
    weekly_update_token = models.CharField(max_length=250, default=None, nullable=True)


class WeeklyUpdateSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        primary_key=True)
    token = models.CharField(max_length=250)
    active = models.BooleanField(default=False)


class UserCreate(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)


class Artist(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name