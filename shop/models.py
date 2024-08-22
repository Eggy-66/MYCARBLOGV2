from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    year = models.IntegerField( default='0')
    power = models.TextField(max_length=50, default='50')
    fuel = models.TextField(max_length=50,default='Benzina')
    cabin_type = models.TextField(max_length=50, default='Sedan')
    phone_number = models.TextField(max_length=15, default = '0')
    photo = models.ImageField(upload_to='media/photo/', blank=True, null=True)
    

    def __str__(self):
        return self.name

class Message(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender} to {self.recipient}'
