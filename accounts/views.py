from django.shortcuts import render , redirect
from .forms import SignupForm
from django.contrib.auth import authenticate , login

# Create your views here.
def signup (requset):
    if requset.method=="POST":
        form = SignupForm(requset.POST)  #for save form 
        #for chieak validation 
        if form.is_valid():
            form .save()
            #  الخطوة الجايه بتستخدم للتحديث السيشن محتاج اليووزر نيم والباسورد 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(requset,user)
            return redirect('/accounts/pfofile')
    
    else: 
        form = SignupForm()  # for view form django
    return render (requset , 'registration/signup.html',{'form':form}) 