from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Group,Contact
from .forms import GroupForm


# # Create your views here.
# class TextMessageModelApi(ModelViewSet):
#     serializer_class = TextMessageSerializer
#     base_name = 'text_messages'

#     def list(self, request, *args, **kwargs):
#         return self.get_queryset()

#     def get_queryset(self):
#         recipients = SmsRecipient.objects.all().order_by("-pk")[:5]
#         json_payload = [SMSRecipientSerializer(recipient).data for recipient in recipients]
#         return Response(json_payload)

#     def create(self, request, *args, **kwargs):
#         logger = get_logger(__name__).bind(
#             action="send_sms_excel"
#         )

#         logger.debug("start")
#         form = UploadSMSExcelForm(request.POST, request.FILES)
#         status_, sms_and_recipients_ = form.is_valid(request)
#         response_ = response.Response()
#         if not status_ and isinstance(sms_and_recipients_, tuple):
#             response_.status_code = status.HTTP_400_BAD_REQUEST
#             response_.data = {"invalid_format": True, "extension": sms_and_recipients_[1]}
#             return response_
#         if isinstance(sms_and_recipients_, bool):
#             response_.status_code = status.HTTP_400_BAD_REQUEST
#             response_.data = {"empty_excel_file": True}
#             return response_
#         message = request.data.get("message")
#         if not message:
#             response_.status_code = status.HTTP_400_BAD_REQUEST
#             excel = {"data": sms_and_recipients_}
#             response_.data = {"message": "Empty message not allowed", "excel": excel, "status": status_}
#             response_.data.update({"data": sms_and_recipients_}) if not status_ else ""
#             return response_
#         if not status_:
#             response_.status_code = status.HTTP_400_BAD_REQUEST
#             excel = {"data": sms_and_recipients_}
#             response_.data = {"excel": excel, "in_valid_excel": True}
#             return response_
#         sender_id = request.data.get("sender_id")

#         if status_:
#             data = {str(message): [(value, key) for key, value in sms_and_recipients_.items()]}

#             user = User.objects.get(username="guest")
#             sms_status, result = create_send_sms_task(sms_sender=user, sms_details=data,
#                                                       sender_id=sender_id)
#             if sms_status:
#                 response_.status_code = status.HTTP_200_OK
#                 return response_
#             else:
#                 response_.status_code = status.HTTP_403_FORBIDDEN
#                 response_.data = sms_status
#                 return response_


def index (request):
    return render (request,'index.html')

def user_page (request):
    return render (request,'user.html')
  
# Create your views here.
def homepage(request):
    groups = Group.get_groups()
    contact = Contact.objects.all()
    if request.method == "POST":
        form = GroupForm(request.POST,request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            # group.contact =contact
            group.save()
        return redirect('homepage')
    else:
        form = GroupForm()
    context = { 'groups': groups, 'form': form}

    return render(request, 'index.html', context )

def group(request, Group):
    groups = Group.get_groups()
    context = {'images':images, 'groups': groups}

    return render(request, 'groups.html', context)

def search_group(request):
    if 'searchgroup' in request.GET and request.GET["searchgroup"]:
        results= request.GET.get("searchgroup")
        searched = Group.search_by_name(results)
        message = f"{results}"

        context = {'found':searched,'message': message}

        return render(request, "search.html",context)
    else:
      message = "You haven't searched for any group"
      return render(request, 'search.html',{"message":message})   
