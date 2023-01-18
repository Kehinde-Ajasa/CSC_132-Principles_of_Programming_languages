from django.shortcuts import render
from . models import User

# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        user = User.objects.create(Email = email)
        user.save()
    return render(request,'Main_Application/index.html')

def csc_admin(request):
    userEmails = User.objects.all()
    return render(request,'Main_Application/csc-admin.html',{'userEmails':userEmails})
