from django.shortcuts import render
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import TalkingForm
import csv
import io
from django.contrib import messages
from .models import Profile

def talking_view(request):
    if request.method == 'POST':
        form = TalkingForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            api_key = form.cleaned_data['api_key']
            recipients = form.cleaned_data['recipients']
            message = form.cleaned_data['message']
            sender_id = form.cleaned_data['sender_id']

            form.save()
            return HttpResponseRedirect('/success_report/')

    else:
        form = TalkingForm()

    context = {'form': form}
    return render(request, "send_sms.html", context)

def success_report(request):
    context = {}
    return render(request, "success.html", context)



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
