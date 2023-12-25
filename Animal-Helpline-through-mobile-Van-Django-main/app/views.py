from django.conf import settings
from django.core import mail
from django.shortcuts import render
from .models import Contact,dead,harassement,injured,Feedback
from django.http import HttpResponse

# Create your views here.
def menu_baar_final(request):
    return render(request,'menu_baar_final.html')

def index(request):
    if request.method=="POST":
        contact=Contact()
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact.email=email
        contact.password=password
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACTING US</h1>")
    return render(request,'index.html')

def deadregistration(request):
    if request.method=="POST":
        contact1= dead()

        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        Address = request.POST.get('Address')
        about = request.POST.get('about')

        contact1.name = name
        contact1.email = email
        contact1.phoneNumber = phoneNumber
        contact1.Address = Address
        contact1.about = about
        contact1.save()
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_message = mail.EmailMessage(f'Email from Animal Helpline',
                                          f'{name} your form is confirmed and the animal will be picked up soon @dead animal pickup service',
                                          from_email, [email], connection=connection)
        connection.send_messages([email_message])
        connection.close()
        return render(request, 'thankyou.html')

    return render(request, 'deadregistration.html')


def ngoregistration(request):
    if request.method == "POST":
        contact2 = harassement()

        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        Address = request.POST.get('Address')
        about = request.POST.get('about')

        contact2.name = name
        contact2.email = email
        contact2.phoneNumber = phoneNumber
        contact2.Address = Address
        contact2.about = about
        contact2.save()
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_message = mail.EmailMessage(f'Email from Animal Helpline',
                                          f'{name} your case is registered and will be solved soon. Thanks for your efforts for prevention of Animal Harassement @ngo team',
                                          from_email, [email], connection=connection)
        connection.send_messages([email_message])
        connection.close()
        return render(request, 'thankyou.html')

    return render(request, 'ngoregistration.html')


def injuredregistration(request):
    if request.method == "POST":
        contact3 = injured()

        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        Address = request.POST.get('Address')
        about = request.POST.get('about')

        contact3.name = name
        contact3.email = email
        contact3.phoneNumber = phoneNumber
        contact3.Address = Address
        contact3.about = about
        contact3.save()
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_message = mail.EmailMessage(f'Email from Animal Helpline',
                                          f'{name} Thank you for your efforts towards helping Animals, Your case will be solved at our earliest @injured animal',
                                          from_email, [email], connection=connection)
        connection.send_messages([email_message])
        connection.close()
        return render(request, 'thankyou.html')

    return render(request, 'injuredregistration.html')

def feedback(request):
    if request.method== "POST":
        contact4=Feedback()
        about = request.POST.get('about')
        contact4.about=about
        contact4.save()
        return render(request, 'thankyou.html')

    return render(request, 'feedback.html')

def term_2(request):
    return render(request, 'term_2.html')

def contactus(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'aboutus.html')