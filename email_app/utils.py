from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject="This email from my side"
    message="this is the test message"
    recepient_list=["vinaysharma5335@gmail.com"]
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject,message,from_email,recepient_list)