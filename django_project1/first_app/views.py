from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# For MTV testing, we need to import models
from first_app.models import Topic, Webpage, AccessRecodrd


def index(request):
    #webpage_list = Webpage.objects.order_by('date')
    webpage_list = AccessRecodrd.objects.order_by('date')
    date_dic = {"acc_recs": webpage_list}
    return render(request, 'first_app\index.html', context=date_dic)

#    return HttpResponse("Hello World!"
     # First application
    '''my_dic = {"insert_me":"Hello This is from first_app's view.py"}
    return render(request, 'first_app\index.html', context=my_dic)'''
#    return HttpResponse("Hello World!"
