import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee
import threading

@receiver(post_save, sender=Employee)
def employee_saved_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received for Employee: {instance.name}")
        time.sleep(5)
        print(f"Signal handler for {instance.name} completed after 5 seconds.")



@receiver(post_save, sender=Employee)
def employee_saved_handler(sender, instance, **kwargs):
    print(f"Signal received for Employee: {instance.name}")
    print(f"Signal handler is running in thread: {threading.current_thread().name}")


@receiver(post_save, sender=Employee)
def employee_post_save_handler(sender, instance, **kwargs):
    instance.status = "Processed"
    instance.save()  # Save to the database
    print(f"Signal: Employee {instance.name}'s status changed to '{instance.status}'")