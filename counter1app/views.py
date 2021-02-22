from django.shortcuts import render
import csv
import io
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
# Create your views here.


def profile_upload(request):
    # I have to declare the template
    template = "profile_upload.html"
    data = Profile.objects.all()

# depending on their context
    prompt = {
        'order': 'Order of the CSV should be first_name,last_name,email,phone',

    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    # checking whether it is a csv file.
    if not csv_file.name.endswith('.csv'):
        message.error(request, 'Check whether this is a CSV file')
    data_set = csv_file.read().decode('UTF-8')

        # setting up a loop for each line
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
            first_name=column[0],
            last_name=column[1],
            email=column[2],
            phone=column[3],
        )
    context = {}
    return render(request, template, context)
# @login_required(login_url='/loginViews')
def addContact(request):
    '''
    adding a contact to be texted
    '''
    if request.method == 'POST':
        new_contact = ProfileForm(request.POST)
            # first_name=request.POST['first_name'],
            # last_name=request.POST['last_name'],
            # email=request.POST['email'],
            # phone=request.POST['phone'],
        if new_contact.is_valid():
            contact = new_contact.save(commit=False)
            contact.save()
            messages.success(request,'Success! Contact added successfully.')
            return redirect('coun:allcontacts')
    else:
        new_contact=ProfileForm()
        # return redirect('add-contact')
        return render(request,'createUser.html',{"new_contact":new_contact})



# def index (request):
#     return render (request,'index.html')
# @login_required(login_url='/loginViews/')
def user_page (request):
    all_contacts = Profile.objects.all()
    
            
    return render (request,'user/user.html',{'data':all_contacts})

def register_user(request):
    current_user = request.user
    if request.method =='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            formUser = form.save(commit=False)
            formUser.user = current_user
            formUser.save()
            return redirect('user_page')
    else:
        form = ProfileForm()
    
    return render(request,"register_user.html",{"formUser":form})

# class delete_contact(DeleteView):
#     model = Profile
#     success_url ="/"
    
class update_contact(UpdateView):
    model = Profile
    template_name = 'user/edit_contact.html'
    fields = ['first_name','last_name','email','phone']
    success_url = reverse_lazy('user_page')
            
