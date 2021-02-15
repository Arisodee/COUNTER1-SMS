from django.shortcuts import render
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
# from twilio.rest import Client
from django.http import HttpResponseRedirect

from .forms import TalkingForm

# def broadcast_sms(request):
#     message_to_broadcast = ("Have you played the incredible TwilioQuest "
#                                                 "yet? Grab it here: https://www.twilio.com/quest")
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
#         if recipient:
#             client.messages.create(to=recipient,
#                                    from_=settings.TWILIO_NUMBER,
#                                    body=message_to_broadcast)from django.http import HttpResponseRedirect



# form view
def talking_view(request):
    if request.method == 'POST':
        form = TalkingForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            api_key = form.cleaned_data['api_key']
            recepients = form.cleaned_data['recepients']
            message = form.cleaned_data['message']
            sender_id = form.cleaned_data['sender_id']
            
            form.save()
            return HttpResponseRedirect('/lets_talk/')

    else:
        form = TalkingForm()

    context = {'form': form}
    return render(request, "send_sms.html", context)


