from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
import os
from .models import Product

@receiver(post_delete, sender=Product)  
def delete_image_from_media(sender, instance, **kwargs):
    # Check if the instance has an image field
    if hasattr(instance, 'image'):  
        # Get the path of the image file
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.image))
        # Check if the image file exists
        if os.path.exists(image_path):
            # Delete the image file
            os.remove(image_path)
