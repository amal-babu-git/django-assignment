from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel, SignalModel
import time
import threading

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print("Signal handler started")
    print(f"Signal handler thread: {threading.current_thread().name}") # required for question 2
    SignalModel.objects.create(description="Signal triggered") # required for question 3
    time.sleep(5) # simulate a long running task
    print("Signal handler finished")
