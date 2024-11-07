from djongo import models
from djongo import models

class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Use hashing for production passwords

    def __str__(self):
        return self.username

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    merchant = models.CharField(max_length=255)
    risk_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.amount} @ {self.merchant}'
from django.db import models

class Transaction(models.Model):
    user_id = models.IntegerField() 
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    timestamp = models.DateTimeField() 
    merchant = models.CharField(max_length=100)  
    risk_score = models.FloatField()  

    def __str__(self):
        return f"Transaction {self.id} - User {self.user_id}: {self.amount} @ {self.merchant}"
