from django.db import models

class Customer(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def register(self):
        self.save()

    @staticmethod

    def get_customer_by_email(email):
        try :
           return Customer.objects.get(email=email)
        except:
           return False
           
    def isExist(self):
        return Customer.objects.filter(email=self.email)

