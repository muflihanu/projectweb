from django.db import models
# Create your models here.
class Usersign_up(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()

class Vendorregister(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=20)
    businessname=models.CharField(max_length=30)
    businnesregistornumber=models.CharField(max_length=5)
    phone = models.CharField(max_length=15) 




class Packagecreate(models.Model):
    vendor = models.ForeignKey(Vendorregister, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=25)
    image=models.ImageField(upload_to='gallery/')
    description=models.CharField(max_length=700)
    date=models.DateField()
    price=models.IntegerField(default=0)
    aprovel=models.BooleanField(default=False)

    def __str__(self):
        return self.title 
    

class Bookingdetails(models.Model):
    user = models.ForeignKey(Usersign_up, on_delete=models.CASCADE,null=True,blank=True)
    fullname=models.CharField(max_length=40)
    package = models.ForeignKey(Packagecreate, on_delete=models.CASCADE,null=True,blank=True)
    number_of_people=models.IntegerField()
    booking_date=models.DateField()
    phone=models.CharField(max_length=15)

    def __str__(self):
     return str(self.package)
    