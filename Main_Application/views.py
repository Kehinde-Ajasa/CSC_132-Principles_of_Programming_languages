from django.shortcuts import render
from . models import User
from email.message import EmailMessage
from django.http import HttpResponse,JsonResponse
import ssl
import smtplib
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
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
    return render(request,'Main_Application/index.html')

@csrf_exempt
def save_user(request):
        user = User.objects.all()
        if request.method == 'POST':
                data = json.loads(request.body)
                field1_Name = data.get('Name')
                field2_Email  = data.get('Email')
                user_saved = User.objects.create(Name = field1_Name, Email =field2_Email)
                # print(sending_email(useremail,username))
                user_saved.save()
                return JsonResponse({'message': 1})
        else:
                return JsonResponse({'message': 0})

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

