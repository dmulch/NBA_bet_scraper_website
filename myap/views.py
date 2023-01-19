from django.http import HttpResponseRedirect
from django.shortcuts import render
from myap import support_functions
from myap.models import Currency, Teams


#from django.http import HttpResponseRedirect
#from django.urls import reverse

# Create your views here.

def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now() #time sitting on the server
    data['time_of_day'] = time
    print(data) #print goes to line here, not browser. must be sent to template.
    return render(request,'home.html',context=data) #wtf is context??

def maintenance(request):
    data = dict()
    try:
        choice = request.GET['selection']
        if choice == "currencies":
            support_functions.add_currencies(support_functions.get_currency_list())
            c_list = Currency.objects.all()
            #print("Got c_list", len(c_list))
            data['currencies'] = c_list
            #return HttpResponseRedirect(reverse('currencies'))
        if choice == 'teams':
            support_functions.add_teams(support_functions.get_teams())
            t_list = Teams.objects.all()
            print('Got t list', len(t_list))
            data['teams'] = t_list
            #return HttpResponseRedirect(reverse('teams'))
        if choice == 'clear':
            for i in Teams.objects.all():
                i.delete()
            print('data delete')
    except:
        pass
    return render(request, "maintenance.html", context=data)

def view_currencies(request):
    data = dict()
    c_list = Currency.objects.all()
    data['currencies'] = c_list
    return render(request,'currencies.html',context=data)

def view_teams(request):
    data = dict()
    t_list = Teams.objects.all()
    data['teams'] = t_list
    return render(request,'teams.html',context=data)