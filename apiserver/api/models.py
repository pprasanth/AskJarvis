from django.db import models

# Create your models here.
class Users(models.Model):
    # title = models.CharField(max_length=200)
    # content = models.TextField()
    # pub_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'