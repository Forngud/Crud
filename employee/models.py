from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=30)  
    ename = models.CharField(max_length=30)  
    eapellido = models.CharField(max_length=30)  
    eemail = models.CharField(max_length=50)  
    econtact = models.CharField(max_length=15) 
    egrado = models.CharField(max_length=30) 
    edireccion = models.CharField(max_length=30)   
    egenero = models.CharField(max_length=30)   


    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee"  