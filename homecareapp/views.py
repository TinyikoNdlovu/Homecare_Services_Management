from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blogsingle(request):
    return render(request, 'blog-single.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        umessage = request.POST['umessage']

        send_mail(
            message_name, # User name
            message_subject, # Message subject
            umessage, # Messages
            message_email, # From email
            ['jesicaalice06@gmail.com'], # To email
        )

        return render(request, 'contact.html', {'message_name': message_name})
    
    else:
        return render(request, 'contact.html', {})
