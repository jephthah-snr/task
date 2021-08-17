from django.shortcuts import render, redirect
from . forms import ContactForm
from django.contrib import messages

def main(request):
    form = ContactForm(request.POST)
    sent = False
    if request.method == 'POST':
    # Form was submitted
        form = ContactForm(request.POST)
        if form.is_valid():
    # Form fields passed validation
            sent = True
            name = form.cleaned_data.get('contact_name')
            messages.success(request,f"thank you {name} for contacting me!, i have recieved your email and i will reply you.") 
            return redirect('home-view')
        else:
            form = EmailPostForm()
            messages.error(request,'the didn"t work chairman!, please try again!') 
    return render(request, 'main/index.html',{'form': form,'sent': sent})


def Contact_form(request):
    pass