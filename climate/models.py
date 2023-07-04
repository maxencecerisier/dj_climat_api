from django.db import models

class Users(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class ClimateImpact(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    carbon_footprint = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.date}'
