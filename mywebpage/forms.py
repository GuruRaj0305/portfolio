from .models import FeedBack
from django import forms


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = "__all__"
        labels = {
            "user_name": "Your name",
            "user_mail_id": "Mail id", 
            "user_mobile_number": "PH no", 
            "user_feedback": "Message"
        }
