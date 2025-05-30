from django.db import models

class Charity(models.Model):
    name = models.CharField(max_length=255)
    mission_statement = models.TextField(max_length=2000)
    website_url = models.URLField()
    contact_email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name