from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    chat_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name
    
class Sub_category(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    image = models.ImageField(upload_to='sub_category/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product/')
    price = models.IntegerField()
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return self.user.username
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    status = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.user.username