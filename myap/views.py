from django.shortcuts import render

# Create your views here.

def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now() #time sitting on the server
    data['time_of_day'] = time
    print(data) #print goes to line here, not browser. must be sent to template.
    return render(request,'home.html',context=data) #wtf is context??