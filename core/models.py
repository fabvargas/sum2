from django.db import models

# Create your models here.


class Country (models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.country_id} | {self.country_name}"
    


class UserType(models.Model):
    user_type_id = models.AutoField(primary_key=True)
    user_type_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.user_type_id} | {self.user_type_name}"
    
   

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.EmailField(max_length=100, unique=True)
    user_password = models.CharField(max_length=100)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id} | {self.user_name} | {self.user_email} | {self.user_type} | {self.country} | {self.city}"


class UserProfile(models.Model):
    user_profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=15)
    user_country = models.ForeignKey(Country, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user_profile_id} | {self.user_name} | {self.user_phone} | {self.user_country} | {self.user_city}"
    
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_id} | {self.product_name} | {self.product_description} | {self.product_price} | {self.product_image}"    
    
    
class Sells(models.Model):
    sells_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return f"{self.sells_id} | {self.product.product_name} | {self.product.product_price}"