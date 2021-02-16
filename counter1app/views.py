from django.shortcuts import render
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import TalkingForm


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




