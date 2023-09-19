from django.shortcuts import render,redirect
from .utils import send_email_to_client

def send_email(request):
    send_email_to_client()
    return redirect('/')
    # return render(request,"email_template.html")
    # #return render(request,"email_sent.html")
    # #D:\Django_project\email_project\email_app\templates\email_template.html
















# email_app/views.py

#from django.core.mail import send_mail


# from django.shortcuts import render

# def send_email(request):
#     recipient_email = 'vinaysharma5335@gmail.com'
#     recipient_name = 'Vinay'
#     subject = 'Sample Email'
#     message = 'This is a sample email sent from a Django project.'
#     from_email = 'vinaysharma5335@gmail.com'  # Your Gmail email address

#     # Render the email content from the template
#     message_html = render(request, 'email_template.html', {'recipient_name': recipient_name})

#     # Send the email
#     send_mail(subject, message, from_email, [recipient_email], html_message=message_html)

#     return render(request, 'email_sent.html')
