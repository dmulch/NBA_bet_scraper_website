from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Currency(models.Model):
    iso = models.CharField(max_length=3)
    long_name = models.CharField(max_length=50)
    def __repr__(self):
        return self.iso + " " + self.long_name
    def __str__(self):
        return self.iso + " " + self.long_name

class Holding(models.Model):
    iso = models.ForeignKey(Currency,on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    buy_date = models.DateField()
    def __repr__(self):
        return self.iso.iso + " " + str(self.value) + " " + str(self.buy_date)
    def __str__(self):
        return self.iso.long_name + " " + str(self.value) + " " + str(self.buy_date)

class Rates(models.Model):
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    x_currency = models.CharField(max_length=3)
    rate = models.FloatField(default=1.0)
    last_update_time = models.DateTimeField()
    def __repr__(self):
        return self.currency.iso + " " + self.x_currency + " " + str(self.rate)
    def __str__(self):
        return self.currency.iso + " " + self.x_currency + " " + str(self.rate)

class Teams(models.Model):
    short_name = models.CharField(max_length=3)
    long_name = models.CharField(max_length=25)
    def __repr__(self):
        return self.long_name + " (" + self.short_name + ")"
    def __str__(self):
        return self.long_name + " (" + self.short_name + ")"


class PastGames(models.Model):
    home_team = models.CharField(max_length=3)
    home_score = models.IntegerField(default=0)
    home_money_line = models.IntegerField(default=0)
    away_team = models.CharField(max_length=3)
    away_score = models.IntegerField(default=0)
    away_money_line = models.IntegerField(default=0)
    game_date = models.DateField()
    def __repr__(self):
        return self.home_team + " " + str(self.home_score) + " " + str(self.home_money_line) + " " + self.away_team + " " + str(self.away_score) + " " + str(self.away_money_line)
    def __str__(self):
        return self.home_team + " " + str(self.home_score) + " " + str(self.home_money_line) + " " + self.away_team + " " + str(self.away_score) + " " + str(self.away_money_line)

class AccountHolder(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    currencies_visited = models.ManyToManyField(Currency)
    def __str__(self):
        return self.user.username
    def __repr__(self):
        return self.user.username

