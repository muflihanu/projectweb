from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout




# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):

    return render(request,"about.html")


def contact(request):

    return render(request,"contact.html")

def vendor(request):

    return render(request,"vendor.html")

def signup(request):
    if request.method == 'POST':
        form=User_signupform(request.POST)
        if form.is_valid():
            usr=form.save(commit=False)
            raw_password=form.cleaned_data.get('password')
            usr.password = make_password(raw_password)
            usr.save()
            return redirect('userlogin')
    else:
      form=User_signupform()
      return render(request,"signup.html",{'form':form})



def userlogin(request):
    if request.method == 'POST':
        form = Userlogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = Usersign_up.objects.filter(username=username).first()
            if user and check_password(password, user.password):
                request.session['user_id'] = user.id 
                return redirect('userhome')

    else:
        form = Userlogin()
    
    return render(request, "userlogin.html", {'form': form})


def userhome(request):
    pk=Packagecreate.objects.all()
    return render(request,"userhome.html",{'package':pk})
    

def uselogout(request):
    logout(request)
    return redirect('home')



def vendorhome(request):
    vendor_id=request.session.get('vuser.id')
    pk = Packagecreate.objects.filter(vendor_id=vendor_id)

    return render(request,"vendorhome.html",{'package':pk})


def vendorsignup(request):
    if request.method == 'POST':
        fm = Vendorregistorform(request.POST)
        if fm.is_valid():
            data = fm.save(commit=False)
            raw_password = fm.cleaned_data.get('password')
            data.password = make_password(raw_password)
            data.save()
            return redirect('vendorlogin')  
        
    else:
        fm = Vendorregistorform()

    return render(request, "vendorsignup.html", {'form': fm}) 
    

def vendorlogin(request):
    if request.method == 'POST':
        form=Vendorlogin(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            vuser=Vendorregister.objects.filter(email=email).first()
            if check_password(password,vuser.password):
                request.session['vuser.id']=vuser.id
                return redirect('vendorhome')
    else:
        form=Vendorlogin()
        return render(request,"vendorlogin.html",{'form':form})

def vendorlogout(request):
    logout(request)
    return redirect('vendorlogin')


def vcreate(request):
    if request.method == 'POST':
        form = vpackageform(request.POST, request.FILES)
        if form.is_valid():
            vendor_id = request.session.get('vuser.id')
            ven = Vendorregister.objects.get(id=vendor_id)  
            p = form.save(commit=False)
            p.vendor = ven 
            p.save()
            return redirect('vendorhome')
    else:
        form = vpackageform()
    return render(request, "vcreate.html", {'form': form}) 

    

def vendordelete(request,pk):
        item=get_object_or_404(Packagecreate,pk=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('vendorhome')

def vendorupdate(request,pk):
    item=get_object_or_404(Packagecreate,pk=pk)
    if request.method == 'POST':
        form=vpackageform(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('vendorhome')
    else:
        form=vpackageform(instance=item)
    return render(request,"update.html",{'form':form})

def booking(request,package_id):
    user_id=request.session.get('user_id')
    package = get_object_or_404(Packagecreate, id=package_id)
    if request.method == 'POST':
        form=Bookingdetailsform(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.package = package  
            booking.user_id = user_id
            booking.save()
            return redirect('payment')
        
    else:
        form=Bookingdetailsform()
    return render(request,"booking.html",{'form': form, 'package': package})


def bookingdisplay(request):
    user_id=request.session.get('user_id')
    print(f'{user_id}')
    booking = Bookingdetails.objects.filter(user_id=user_id)
    print(f'{booking}')
    return render(request, "bookingdisplay.html", {'booking': booking})



def vendorbookings(request):
    vendor_id=request.session.get('vuser.id')
    print(f'{vendor_id}')
    package =Packagecreate.objects.filter(vendor_id=vendor_id) 
    print(f'{package}')
    booking=Bookingdetails.objects.filter(package__in=package) 
    print(f'{booking}')
    return render(request, "vendorbookings.html", {'booking': booking})

def profile(request):
    user_id=request.session.get('user_id')

    form=Usersign_up.objects.filter(id=user_id)
    return render(request,"profile.html" ,{'form':form})


def payment(request):
    return render(request,"payment.html")