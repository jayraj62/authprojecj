from django.shortcuts import redirect, render
from .forms import userform,notesForm,contform
from .models import usersignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from authproject import settings

# Create your views here.
def newuser(request):
    ufrom=userform(request.POST)
    if ufrom.is_valid():
        ufrom.save()
        print("Signup successfull")
        sub='Login Successfull'
        msg='Welcome to our new project/nJayrajsinh Mori/n+91 7788996655 '
        frm=settings.EMAIL_HOST_USER
        to_mail=['jayrajmori111@gmail.com','sanketbarot74@gmail0.com','jugalgajjar11@gmail.com']
        send_mail(sub,msg,frm,to_mail)
        
        return redirect('/') 
    else:
        print(ufrom.errors)

def userlogin(request):
    unm=request.POST["uname"]
    pas=request.POST["password"]

    userID=usersignup.objects.get(uname=unm)
    print("Userid:",userID.id) 
    user=usersignup.objects.filter(uname=unm,password=pas)


    if user:
        print('Login successfull')
        

        request.session["user"]=unm
        request.session["userid"]=userID.id
    else:
        print("'Login Failed")

def notesupload(request):
    notefrm=notesForm(request.POST,request.FILES)
    if notefrm.is_valid():
        notefrm.save()
        print("Notes uploaded successfull")
    else:
        print(notefrm.errors)



def index(request):
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            newuser(request)
            return redirect('notes')
                
        elif request.POST.get("login")=="login":
            userlogin(request)
           
           
            return redirect('notes')
            
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def notes(request):
    if request.method=='POST':
        if request.POST.get("postnote")=="postnote":
            notesupload(request)
            return redirect('notes')

        if request.POST.get("signup")=="signup":
            newuser(request)
            return redirect('notes')
        elif request.POST.get("login")=="login":
            userlogin(request)
            return redirect('notes')
    user=request.session.get("user")   
    return render(request,'notes.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def profile(request):
    user=request.session.get("user")  
    userid=request.session.get("userid") 
    id=usersignup.objects.get(id=userid)
    if request.method=='POST':
        userupdate=userform(request.POST)
           
        if userupdate.is_valid:
            userupdate=userform(request.POST,instance=id)
            userupdate.save()          
            print("Profile has been updated Successfully..!")
            return redirect('/')
        else:
            print(userupdate.errors)    

    return render(request,'profile.html',{'user':user,'userid':usersignup.objects.get(id=userid)})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        cntfrm=contform(request.POST)
        if cntfrm.is_valid:
           cntfrm.save()
           print("Data saved")
           return redirect('/')
        else:
            print(cntfrm.errors)
    return render(request,'contact.html')
