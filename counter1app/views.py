from django.shortcuts import render
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from .forms import TalkingForm

import csv
import io
from django.contrib import messages
from .models import Profile,Add_user

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from .models import Count
from django.http import JsonResponse
from validate_email import validate_email
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.tokens import PasswordResetTokenGenerator

import threading

from django.contrib.auth.decorators import login_required

from .forms import Add_userForm,EditSupervisor
from django.contrib.auth import logout
from django.views.generic import (DetailView)



@login_required
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

def index(request):
    return render(request,'index.html')




class EmailThread(threading.Thread):

    def __init__(self, email_message):
        self.email_message = email_message
        threading.Thread.__init__(self)

    def run(self):
        self.email_message.send()


class RegistrationView(View):
    def get(self, request):
        return render(request, 'registration/register.html')
    def post(self, request):
        context = {
            'data': request.POST,
            'has_error': False
        }
        email = request.POST.get('email')
        username = request.POST.get('username')
        full_name = request.POST.get('name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'passwords should be atleast 6 characters long')
            context['has_error'] = True
        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'passwords dont match')
            context['has_error'] = True
        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Please provide a valid email')
            context['has_error'] = True
        try:
            if User.objects.get(email=email):
                messages.add_message(request, messages.ERROR, 'Email is taken')
                context['has_error'] = True
        except Exception as identifier:
            pass
        try:
            if User.objects.get(username=username):
                messages.add_message(
                    request, messages.ERROR, 'Username is taken')
                context['has_error'] = True
        except Exception as identifier:
            pass
        if context['has_error']:
            return render(request, 'registration/register.html', context, status=400)
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.first_name = full_name
        user.last_name = full_name
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        email_subject = 'Active your Account'
        message = render_to_string('registration/activate.html',
                                   {
                                       'user': user,
                                       'domain': current_site.domain,
                                       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                       'token': generate_token.make_token(user)
                                   }
                                   )
        email_message = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]
        )
        EmailThread(email_message).start()
        messages.add_message(request, messages.SUCCESS,
                             'account created succesfully')
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        context = {
            'data': request.POST,
            'has_error': False
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '':
            messages.add_message(request, messages.ERROR,
                                'Username is required')
            context['has_error'] = True
        if password == '':
            messages.add_message(request, messages.ERROR,
                                 'Password is required')
            context['has_error'] = True
        user = authenticate(request, username=username, password=password)

        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR, 'Invalid login')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'registration/login.html', status=401, context=context)
        login(request, user)
        return redirect('home')


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 'account activated successfully')
            return redirect('login')
        return render(request, 'registration/activate_failed.html', status=401)


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')



class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Logout successfully')
        return redirect('login')


class RequestResetEmailView(View):
    def get(self, request):
        return render(request, 'registration/request-reset-email.html')

    def post(self, request):
        email = request.POST['email']

        if not validate_email(email):
            messages.error(request, 'Please enter a valid email')
            return render(request, 'registration/request-reset-email.html')

        user = User.objects.filter(email=email)

        if user.exists():
            current_site = get_current_site(request)
            email_subject = '[Reset your Password]'
            message = render_to_string('registration/reset-user-password.html',
                                       {
                                           'domain': current_site.domain,
                                           'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                                           'token': PasswordResetTokenGenerator().make_token(user[0])
                                       }
                                       )

            email_message = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )

            EmailThread(email_message).start()

        messages.success(
            request, 'We have sent you an email with instructions on how to reset your password')
        return render(request, 'registration/request-reset-email.html')


class SetNewPasswordView(View):
    def get(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))

            user = User.objects.get(pk=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.info(
                    request, 'Password reset link, is invalid, please request a new one')
                return render(request, 'registration/request-reset-email.html')

        except DjangoUnicodeDecodeError as identifier:
            messages.success(
                request, 'Invalid link')
            return render(request, 'registration/request-reset-email.html')

        return render(request, 'registration/set-new-password.html', context)

    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token,
            'has_error': False
        }

        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'passwords should be at least 6 characters long')
            context['has_error'] = True
        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'passwords don`t match')
            context['has_error'] = True

        if context['has_error'] == True:
            return render(request, 'registration/set-new-password.html', context)

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))

            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()

            messages.success(
                request, 'Password reset success, you can login with new password')

            return redirect('login')

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, 'Something went wrong')
            return render(request, 'auth/set-new-password.html', context)

        return render(request, 'auth/set-new-password.html', context)
        
#function to send messages using africastalking API

def talking_view(request):
    if request.method == 'POST':
        form = TalkingForm(request.POST)
        if form.is_valid():
            recipients = form.cleaned_data['recipients']
            message = form.cleaned_data['message']            
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


def index(request):
    return render(request,'index.html')


def dashboard(request):
    return render(request, 'simple_sidebar.html')


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



def user_page (request):
    return render (request,'user.html')



# Create your views here.

def user_list(request):
    users = Add_user.objects.filter()
    return render(request,'user_list.html',{'users':users})


def create_user(request):
    '''
    View function to add a new supervisor
    '''
    if request.method == 'POST':
        form = Add_userForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)

            '''
            above line of code displays a user registered in a specific sacco or orgamisation by counter1
            '''
            user.save()
            messages.success(request, f'Congratulations! You have succesfully Added a new User!')
            return redirect('/user_list/')
    else:
        form = Add_userForm()
    return render(request, 'create_user.html', {"form": form})




def edit_superlist(request, supervisor_id):
    '''
    View function to edit an instance of a supervisor/user already created by the admin
    '''
    supervisor = Add_user.objects.get(pk=supervisor_id)
    if request.method == 'POST':
        form = EditSupervisor(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success! Your edit has been successful!')
            return redirect('/user_list/')
    else:
        form = EditSupervisor(instance=supervisor)
    return render(request, 'edit_user.html', {"form": form, "supervisor":supervisor})
