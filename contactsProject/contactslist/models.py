from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_Name = models.CharField(max_length=200)
    last_Name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    # CharField -> VARCHAR

    def to_string(self):
        # return "<td>"+self.first_Name+self.last_Name+"</td><td>"+self.email+"</td><td>"+self.comment+"</td>"
        return "<strong>Name: </strong>"+self.first_Name + self.last_Name+"</br><strong>Email: </strong>"+self.email+"</br><strong>Comment: </strong>"+self.comment+"</br></br>"
    