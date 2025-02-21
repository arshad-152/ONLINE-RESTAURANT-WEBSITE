from django.db import models

# Create your models here.

class ItemList(models.Model):
    Category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name = models.CharField(max_length=30)
    Description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList,on_delete=models.CASCADE,related_name="Name")
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    Username = models.CharField(max_length=20)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()

    def __str__(self):
        return self.Username


class Book_table(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    
    def __str__(self):
        return self.Name
    

class UserInfo(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=20)

