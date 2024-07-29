from django import forms
from .models import Feedback , Contact

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email', 'message']

    def send_email(self):
        """Send the feedback email asynchronously."""
        from .tasks import send_feedback_email_task
        send_feedback_email_task.delay(self.cleaned_data["email"], self.cleaned_data["message"])




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact_no', 'message'] 
