from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('CSC-ADMIN',views.csc_admin,name="csc_admin"),
    path('ADMIN-MESSAGE',views.admin_message,name = 'admin_message'),
]