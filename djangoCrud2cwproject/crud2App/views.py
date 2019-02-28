from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from .forms import NewContactForm
from .models import  Contact

# Create your views here.
def index(request): # read and list all contacts
    allcontacts = Contact.objects.all()
    return render(request, "crud2App/index.html", {'contact_list': allcontacts})
    # return HttpResponse('made it')

# This page will provide a form to add users
def contacts(request):
    new_form = NewContactForm(request.POST or None)
    if new_form.is_valid():#if not valid it skips what is below and goes back to page below
        new_form.save()
        return redirect('index')#redirect goes to another page
    # injecting...
    return render(request, 'crud2App/contacts.html', {'contactform': new_form})
# this function is used to update contacts
def editcontact(request, id):
    user = get_object_or_404(Contact, pk=id)
    edit_form = NewContactForm(request.POST or None, instance=user)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')
    return render(request, 'crud2App/contacts.html', {'contactform': edit_form})
# this function is used to delete contacts
def deletecontact(request,id):
    user = get_object_or_404(Contact, pk=id)
    if request.method == 'POST':
        contacts.delete()
        return redirect('index')

    return render(request, 'crud2App/delete.html', {'selectedcontacts': contacts })

