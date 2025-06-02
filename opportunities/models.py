from django.db import models

# Create your models here.
class Opportunity(models.Model):
    charity = models.ForeignKey(
        to='charities.Charity', # appname.ModelName - This refers to the table that this id can be found in
        related_name='opportunities', # This field details where these opportunities will be available on the foreign object
        on_delete=models.CASCADE # on delete of the charity, CASCADE will delete this opportunity and all other opportunities linked to the deleted charity
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title