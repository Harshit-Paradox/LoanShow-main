from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task(name= "shared_task")
def sub(x,y):
    sleep(10)
    return x-y




@shared_task
def send_feedback_email_task(email, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "support@example.com",
        [email],
        fail_silently=False,
    )

