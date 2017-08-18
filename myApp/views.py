from django.shortcuts import render, redirect
#from django.http import HttpResponse, JsonResponse
from myApp.forms import AddForm
from myApp.models import UserAccount
from django.contrib import messages

# Create your views here.

def renderHome(request):
    context = {}
    return render(request, 'myApp/index.html', context)


def getList(request):
    context = {
        'records': UserAccount.objects.all()
    }
    return render(request, 'myApp/list.html', context)


def getAdd(request):
    add_form = AddForm()
    context = {
        'add_form': add_form
    }
    if request.method == 'POST':
        user = None
        add_form = AddForm(data = request.POST)
        rp = request.POST
        
        if add_form.is_valid():   
            user = UserAccount.objects.create(name = rp['name'], email = rp['email'], )
            user.save()
            if user:
                messages.success(request, 'Your details have been saved')
            else:
                messages.warning(request, 'something went wrong acount not created!! please try again!')
        else:
            context['add_form'] = AddForm(data = request.POST)
    return render(request, 'myApp/add.html', context)


