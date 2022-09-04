from django.db.models import Model,CharField,IntegerField,AutoField,EmailField,DateField

# Create your models here.

class Test(Model):
    
    id = AutoField(primary_key=True)
    name = CharField("name",max_length=20,null=False)
    email = EmailField("email",max_length=50,null=False)
    registration = DateField("registration",auto_now=True,null=False)
    active = CharField("active",max_length=3,null=False)