from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from foodhut_pro.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
import uuid
import os

# Create your views here.
def index(request):
    return render(request,'index.html')
def registration(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['fullname']
            un=a.cleaned_data['username']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            g=a.cleaned_data['gender']
            ps=a.cleaned_data['password']
            cs=a.cleaned_data['cpassword']
            b=regmodel(fullname=fn,username=un,email=em,phone=ph,gender=g,password=ps)

            if ps==cs:
                b.save()
                return redirect(login)
            else:
                return HttpResponse('registration failed')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        x=logform(request.POST)
        if x.is_valid():
            un=x.cleaned_data['username']
            ps=x.cleaned_data['password']
            y=regmodel.objects.all()
            for i in y:
                if un==i.username and ps==i.password:
                    em=i.email
                    return render(request,'restprofile.html',{'username':un,'email':em})
            else:
                return HttpResponse("login failed")
    else:
        return render(request,'login.html')

def regis(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        #checking
        if User.objects.filter(username=username).first():#the first function which takes a query set and returns the first element or nun if query set was empty
            messages.success(request,'username already taken')
        if User.objects.filter(email=email).first():
            messages.success(request,'email already exist')
            return redirect(regis)
        user_obj=User(username=username,email=email)
        user_obj.set_password(password)#set password is a function that sets the user password to the given row string,taking care of the password hashing
        user_obj.save()
        #import uuid
        auth_token=str(uuid.uuid4())#uuid=universly unique identifiers, this module provides immutable uuid objects, uuid has 4 versions, uuid1,uuid3,uuid4,uuid5, uuid4=create random uuid
        profile_obj=usermodel.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)
        return render(request,'sucess.html')
    return render(request,'reg.html')

def send_mail_regis(email,token):
    subject='your account has been verified'
    message=f'paste the link verify your account http://127.0.0.1:8000/foodhut_app/verify/{token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def verify(request,auth_token):
    profile_obj=usermodel.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account is already verfied ')
            return redirect(userlogin)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(userlogin)
    else:
        return HttpResponse("user not found")

def userlogin(request):
    if request.method=='POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user_obj =User.objects.filter(username=username).first()
       if user_obj is None:
           messages.success(request,'user not found')
           return redirect(userlogin)
       profile_obj = usermodel.objects.filter(user=user_obj).first()
       if not profile_obj.is_verified:
           messages.success(request,'profile is not verified check your mail')
           return redirect(userlogin)
       user =authenticate(username=username,password=password)
       if user is None:
           messages.success(request,'wrong password')
           return redirect(userlogin)
       return redirect(userprofile)
    return render(request,'log.html')



def nfile(request):
    if request.method=='POST':
        a=nonform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['nitem']
            np=a.cleaned_data['nprice']
            de=a.cleaned_data['ndes']
            im=a.cleaned_data['nimage']
            b=nonmodel(nitem=nm,nprice=np,ndes=de,nimage=im)
            b.save()
            return redirect(nondisplay)
        else:
            return HttpResponse("file upload failed")
    else:
        return render(request,"nondisplay.html")


def vfile(request):
    if request.method=='POST':
        a=vegform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['vitem']
            np=a.cleaned_data['vprice']
            de=a.cleaned_data['vdes']
            im=a.cleaned_data['vimage']
            b=vegmodel(vitem=nm,vprice=np,vdes=de,vimage=im)
            b.save()
            return redirect(vegdisplay)
        else:
            return HttpResponse("file upload failed")
    else:
        return render(request,"display.html")

def nondisplay(request):
   x=nonmodel.objects.all()
   li=[]
   item=[]
   price = []
   des1=[]
   id=[]

   for i in x:
       path=i.nimage
       li.append(str(path).split("/")[-1])
       nm=i.nitem
       item.append(nm)
       pri=i.nprice
       price.append(pri)
       dis=i.ndes
       des1.append(dis)
       id1=i.id
       id.append(id1)
   mylist=zip(li,item,price,des1,id)
   return render(request,'restdisplay.html',{'mylist':mylist})


def vegdisplay(request):
   x=vegmodel.objects.all()
   li=[]
   item=[]
   price = []
   des1=[]
   id=[]

   for i in x:
       path=i.vimage
       li.append(str(path).split("/")[-1])
       nm=i.vitem
       item.append(nm)
       pri=i.vprice
       price.append(pri)
       dis=i.vdes
       des1.append(dis)
       id1=i.id
       id.append(id1)
   mylist=zip(li,item,price,des1,id)
   return render(request,'rest_vegdisplay.html',{'mylist':mylist})

def vegedit(request,id):
    veg=vegmodel.objects.get(id=id)
    li=str(veg.vimage).split('/')[-1]
    if request.method =="POST":
        if len(request.FILES) != 0:
            if len(veg.vimage) > 0:
                os.remove(veg.vimage.path)
            veg.vimage=request.FILES['vimage']
        veg.vitem=request.POST.get('vitem')
        veg.vdes=request.POST.get('vdes')
        veg.vprice=request.POST.get('vprice')
        veg.save()
        return redirect(vegdisplay)
    context={'veg':veg,'li':li}
    return render(request,'veg_edit.html',context)

def vegdelete(request,id):
    veg=vegmodel.objects.get(id=id)
    if len(veg.vimage) > 0:
        os.remove(veg.vimage.path)
    veg.delete()
    return redirect(vegdisplay)


def nonvegedit(request,id):
    veg=nonmodel.objects.get(id=id)
    li=str(veg.nimage).split('/')[-1]
    if request.method =="POST":
        if len(request.FILES) != 0:
            if len(veg.nimage) > 0:
                os.remove(veg.nimage.path)
            veg.nimage=request.FILES['nimage']
        veg.nitem=request.POST.get('nitem')
        veg.ndes=request.POST.get('ndes')
        veg.nprice=request.POST.get('nprice')
        veg.save()
        return redirect(nondisplay)
    context={'veg':veg,'li':li}
    return render(request,'nonveg_edit.html',context)


def nonvegdelete(request,id):
    veg=nonmodel.objects.get(id=id)
    if len(veg.nimage) > 0:
        os.remove(veg.nimage.path)
    veg.delete()
    return redirect(nondisplay)

def add_details(request):
    if request.method=='POST':
        a=adddetails(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['rimage']
            un=a.cleaned_data['rid']
            em=a.cleaned_data['rname']
            ph=a.cleaned_data['rno']
            g=a.cleaned_data['rloc']
            ps=a.cleaned_data['ropen']
            cs=a.cleaned_data['rclose']
            b=adddetailsmodel(rimage=fn,rid=un,rname=em,rno=ph,rloc=g,ropen=ps,rclose=cs)
            b.save()
            return redirect(contactdisplay)
        else:
            return HttpResponse('details not added')
    return render(request,'add_more_details.html')


def contactdisplay(request):
   x=adddetailsmodel.objects.all()
   for i in x:
       image=(str(i.rimage).split('/')[-1])
       id=i.id
       mid=i.rid
       name=i.rname
       ph_no=i.rno
       location=i.rloc
       open_tym=i.ropen
       close_tym=i.rclose
   return render(request,'contact_display.html',{'id':id,'image':image,'mid':mid,'name':name,'ph_no':ph_no,'location':location,'open_tym':open_tym,'close_tym':close_tym})


def displayedit(request,id):
    dis=adddetailsmodel.objects.get(id=id)
    li=str(dis.rimage).split('/')[-1]
    if request.method =="POST":
        if len(request.FILES) != 0:
            if len(dis.rimage) > 0:
                os.remove(dis.rimage.path)
            dis.rimage=request.FILES['rimage']
        dis.rid=request.POST.get('rid')
        dis.rname=request.POST.get('rname')
        dis.rno=request.POST.get('rno')
        dis.rloc = request.POST.get('rloc')
        dis.ropen = request.POST.get('ropen')
        dis.rclose = request.POST.get('rclose')
        dis.save()
        return redirect(contactdisplay)
    context={'dis':dis,'li':li}
    return render(request,'display_edit.html',context)

def userprofile(request):
    a=usermodel.objects.all()
    for i in a:
        uname=i.user
    return render(request,'userprofile.html',{'uname':uname})
