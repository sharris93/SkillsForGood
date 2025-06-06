from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Charity(models.Model):
    owner = models.ForeignKey(
        to="users.User", # The model this id is related to
        related_name="charities", # How we will populate this charity on the foreign model
        on_delete=models.CASCADE # delete this object if the relation is deleted
    )
    name = models.CharField(max_length=255)
    mission_statement = models.TextField(max_length=2000)
    website_url = models.URLField()
    contact_email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='django_test/', blank=True, storage=MediaCloudinaryStorage)

    def __str__(self):
        return self.name