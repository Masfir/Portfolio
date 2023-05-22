from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact,Blogs
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login to access this page.")
        return redirect("/app/login/")
    
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()           
    #     fname = request.POST.get("name")
    #     femail = request.POST.get("email")
    #     fphonenumber = request.POST.get("num")
    #     fdescription = request.POST.get("desc")      
    #     query  = Contact(name=fname,email=femail,phonenumber=fphonenumber,description=fdescription)
    #     query.save()
    #     # messages.info(request, f'The name is {fname}. The email is {femail}. The phone number is {fphonenumber}. The description is {fdescription}.')
        messages.success(request, "Thanks for contacting us. We will get by you soon!")
        return redirect("/contact")  
    
    context ={
        'contact_form': contact_form
    }  
        
    return render(request,"contact.html",context)

def contact_details(request):
    p = Contact.objects.all()
    context={
       'p': p
       
    }
    return render(request,"contactdetails.html",context)

def handleblog(request):
    posts=Blogs.objects.all()
    context={
       'posts': posts
    }
    return render(request,"handleblock.html",context)

def update(request,id):
    contact_object_id = Contact.objects.get(id=id)
    # print(contact_object_id)
    update_form = ContactForm(instance=contact_object_id)
    
    if request.method == "POST":
        update_form = ContactForm(request.POST, instance=contact_object_id)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, "Thanks for updating!")  
            return redirect('contact_details')
        
    
    context={
        'update_form': update_form
    }
    return render(request,"update_page.html",context)


def delete(request,id):
    delete_object_id = Contact.objects.get(id=id)
    delete_object_id.delete()
    messages.success(request, "Thanks for deleting!")  
    return redirect("/contact_details")

def contact_search(request): 
    search_contact_item = request.GET.get('search_item')
    # print(search_contact_item)
    p = Contact.objects.filter(name__icontains = search_contact_item)
    context={
        'p':p       
    }
    return render(request,"contactdetails.html",context)

def contact_search_id(request): 
    min_id= request.GET.get('min_id')
    max_id= request.GET.get('max_id')
    # print(search_contact_item)
    p = Contact.objects.filter(id__range = (min_id, max_id))
    context={
        'p':p       
    }
    return render(request,"contactdetails.html",context)

def google_map(request):
    return render(request,'googlemap.html')

    
    
    