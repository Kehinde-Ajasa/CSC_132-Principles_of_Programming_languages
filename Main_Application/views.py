from django.shortcuts import render
from . models import User
from email.message import EmailMessage
import ssl
import smtplib
from django.contrib import messages
# Create your views here.

def sending_email(mail,name):
    email_sender = "csc132.collaborators@gmail.com"
    email_password = "avwpgyatfxhdcogw"
    email_receiver = mail
    subject = "Confirmation Mail"
    body = f"""Dear {name}, your Email and registration process has been confirmed.
    Thank you for using our Software."""
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def index(request):
    if request.method == 'POST':
        username =  request.POST['user_name']
        useremail = request.POST['user_email']
        user = User.objects.create(Name = username, Email = useremail)
        print(sending_email(useremail,username))
        messages.info(request,'Thank you, your email is being confirmed')   
        user.save()
    return render(request,'Main_Application/index.html')

def sending_general_email(email_receivers,email_subject,email_body):
        for email_receiver in email_receivers:
                email_sender = "csc132.collaborators@gmail.com"
                email_password = "avwpgyatfxhdcogw"
                email_receiver = email_receiver.Email
                subject = email_subject
                body = email_body
                em = EmailMessage()
                em["From"] = email_sender
                em["To"] = email_receiver
                em['subject'] = subject
                em.set_content(body)

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                        smtp.login(email_sender, email_password)
                        smtp.sendmail(email_sender, email_receiver, em.as_string())

def admin_message(request):
        users = User.objects.all()
        if request.method == 'POST':
                messageSubject = request.POST['subject']
                adminmessage =  request.POST['adminmessage'] 
                messages.info(request,'Message has been sent')   
                print(sending_general_email(users,messageSubject,adminmessage))
        return render(request,'Main_Application/admin-msg.html')

def csc_admin(request):
    userEmails = User.objects.all()
    return render(request,'Main_Application/csc-admin.html',{'userEmails':userEmails})

