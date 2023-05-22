from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        get_name = request.POST.get("name")
        get_email = request.POST.get("email")
        get_password = request.POST.get("password")
        get_confirm_password = request.POST.get("confirm_password")       
        get_name = get_name.title()
        
        if get_password != get_confirm_password:
            messages.info(request, "Password is not matching. Please enter the correct password.")
            return redirect("/app/signup/")
        
        try:
            if User.objects.get(username = get_name):
                messages.warning(request, f"{get_email} email is taken")
                return redirect("/app/signup/")
        
        except Exception as identifier:
            pass    
          
        myuser = User.objects.create_user(get_name, get_email, get_password)
        myuser.save()
        messages.success(request, "User is created. Please Login.")
        return redirect("/app/login/")
                   
    return render(request,'signup.html')

def handleLogin(request):
    if request.method == "POST":
        get_name = request.POST.get("name")
        get_email = request.POST.get("email")
        get_password = request.POST.get("password")
        myuser = authenticate(username = get_name, useremail = get_email, password = get_password)
        
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid")
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "Logout successful")
    return render(request, 'login.html')

# def reverse_pgm(request):
#     if request.method == 'POST':
#         get_input = request.POST.get('inp')
#         print(get_input)
#         output = get_input[::-1]
#         print(output)
        
#         context={
#             "get_input": get_input, 
#             "output": output,
#             }      
#     return render(request,'home.html', context)
