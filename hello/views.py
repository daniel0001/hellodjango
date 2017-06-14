from django.shortcuts import render
from .models import Contact

# Create your views here.
def say_hello(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contact_list':  contacts})

def add_contact(request):
    if request.method == "POST":
        new = Contact()
        new.first_name = request.POST.get('first_name')
        new.last_name = request.POST.get('last_name')
        new.mobile = request.POST.get('mobile')
        new.email = request.POST.get('email')

        new.save()

        return render(request, 'contact-added.html', {'contact': new})
    else:
        return render(request, 'add-contact.html')