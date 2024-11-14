from django.db import models

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('Customer', 'Customer'),
        ('DeliveryPartner', 'DeliveryPartner'),
        ('RestaurantOwner', 'RestaurantOwner'),
        ('RestaurantEmployee', 'RestaurantEmployee'),
        ('FranchiseOwner', 'FranchiseOwner'),
        ('FranchiseEmployee', 'FranchiseEmployee'),
        ('Admin', 'Admin'),
        ('AdminEmployee', 'AdminEmploy')
    ]
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    is_owner = models.BooleanField(default=False)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # franchise = models.ForeignKey('franchise.Franchise', on_delete=models.SET_NULL, null=True, blank=True)
    # restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.SET_NULL, null=True, blank=True)
    # franchise_id = models.ReferenceField
    # merchant_id = models.IntegerField
    
    # def __str__(self):
    #     return self.username
    
    # class Meta:
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'
    #     ordering = ['-created_at']
