from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name=models.CharField('Event Name',max_length=120)
    event_date=models.DateTimeField('Date')
    venue=models.CharField('Venue', max_length=50)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name
