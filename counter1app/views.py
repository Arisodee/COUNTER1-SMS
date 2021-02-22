from django.shortcuts import render,redirect
from django.http import HttpResponse
# from .models import Group,Contact
from .forms import TalkingForm

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

#sending sms users side 

def talking_view(request):
    if request.method == 'POST':
        form = talkingForm(request.POST)
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
    return render(request, "sms.html", context)

def success_report(request):
    context = {}
    return render(request, "delivered.html", context)