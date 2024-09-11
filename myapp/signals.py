from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import time
import threading

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print("Signal handler started")
    print(f"Signal handler thread: {threading.current_thread().name}")
    time.sleep(5) # simulate a long running task
    print("Signal handler finished")
