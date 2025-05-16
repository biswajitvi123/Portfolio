from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')
        send_mail(
            subject,f'From {name} \n {msg} \n Contact us: \n email : {email} Mobile : {mobile}',
            'darksimmon1@gmail.com',
            ['nihalgt220@gmail.com'],
                        
        )

    return render(request,'index.html')