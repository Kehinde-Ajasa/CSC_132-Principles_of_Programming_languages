from django.shortcuts import render
from . models import User
from email.message import EmailMessage
import ssl
import smtplib
# Create your views here.


def sending_email(mail):
    email_sender = "csc132.collaborators@gmail.com"
    email_password = "avwpgyatfxhdcogw"
    email_receiver = mail
    subject = "Confirmation Mail"
    body = """Your Email and registration process has been confirmed.
    Thank you for using our Software."""
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        return smtp.sendmail(email_sender, email_receiver, em.as_string())

def index(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        user = User.objects.create(Email = email)
        print(sending_email(email))
        user.save()
    return render(request,'Main_Application/index.html')




def csc_admin(request):
    userEmails = User.objects.all()
    return render(request,'Main_Application/csc-admin.html',{'userEmails':userEmails})

