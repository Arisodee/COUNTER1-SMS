from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Group,Profile
from .forms import GroupForm
from django.views.generic import UpdateView,DeleteView,View
from django.http import JsonResponse

def index (request):
    return render (request,'index.html')

def user_page (request):
    groups = Group.get_groups()
    all_contacts = Profile.objects.all()
    if request.method == "POST":
        form = GroupForm(request.POST,request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
        return redirect('user_page')
    else:
        form = GroupForm()
    context = { 'groups': groups, 'form': form}
    
    return render (request,'user/user.html',context)

def search_results(request):
    if 'group' in request.GET and request.GET["group"]:
        search_term= request.GET.get("group")
        searched_groups = Group.search_by_name(search_term)
        message = f"{search_term}"

        context = {'groups':searched_groups,'message': message}

        return render(request, "user/search.html",context)
    else:
      message = "You haven't searched for any group"
      return render(request, 'user/search.html',{"message":message})   

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'user/Update.html'   
    fields= ['name','contact']  
    success_url = ('/')  

def updategroup(request):
    form = GroupForm()
    context = {'form' : form}
    return render(request, 'user/update.html', context)    

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'user/delete.html'
    success_url = ('/')

def deleteForm(request):
    context ={     
    }
    return render(request ,'user/delete.html', context )

def deletegroup(request):
    context = {'object:title' : group}
    return render(request, 'user/delete.html', context)

class SmsNumJsonView(View):
    def get(self,*args, **kwargs):
        sms_count = Profile.objects.filter().count()
        return JsonResponse({'sms_count':sms_count})
