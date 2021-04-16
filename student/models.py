
from django.db import models
#DataFlair Models
class STUDENT(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    contact = models.CharField(max_length = 12)
    email = models.EmailField(blank = True)
    address= models.TextField()
    def __str__(self):
        return self.name