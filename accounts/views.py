from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Account

# Create your views here.
def test(request):
    return render(request,'index.html') 

def resume(request):
    if request.method == 'POST':
        user = request.user
        account = Account.objects.get(user=user)
        file = request.FILES['file']
        account.resume = file
        account.save()
        return redirect('/')
    else:
        return render(request,'resume.html')

# def check_resume(request):
#     user = request.user
#     account = Account.objects.get(user=user)
#     print(account.resume)
#     pass


def logout(request):
    auth.logout(request)
    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            account = Account.objects.get(user=user)
            if account.resume.name :
                return redirect('/')
            else:
                return redirect('resume')
        else:
            messages.info(request,'INVALID CREDENTIALS')
            return redirect('login')    


    else:
        return render(request,'signin.html')   


def register(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'USERNAME TAKEN')
                print("fuckusername")
                return redirect('register')

            elif Account.objects.filter(email=email).exists():    
                messages.info(request,'EMAIL TAKEN')
                return redirect('register')

            elif len(email) == 0:    
                messages.info(request,'EMAIL MISSING')
                return redirect('register')
            
            elif len(name) == 0:       
                messages.info(request,'FIRST NAME MISSING')
                return redirect('register')

            elif len(password1) == 0: 
                messages.info(request,'PASSWORD CANNOT BE EMPTY!!')
                return redirect('register')

            elif len(password1) < 8:
                messages.info(request,'PASSWORD SHOULD OF 8 CHARACTERS!!')
                return redirect('register')

            else:    
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                account = Account(name=name, email=email, user=user)
                account.save()
                messages.info(request,'USER CREATED')
                return redirect('login')

        else:
            messages.info(request,'PASSWORD NOT MATCHING!!')
            return redirect('register')

        return redirect('/')

    else:
       return render(request,'signup.html')