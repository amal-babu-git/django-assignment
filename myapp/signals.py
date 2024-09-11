from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import time

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5) # simulate a long running task
    print("Signal handler finished")
    