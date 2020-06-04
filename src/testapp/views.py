from django.shortcuts import render
from django.http import HttpResponse
from .models import Userrequests
import testapp.browser_cleaner as bc
from datetime import datetime
# Create your views here.

def test(request):
    # Создание базы данных 
    # query_lst = bc.parsing()
    # for line1 in query_lst:
    #     Userrequests.objects.create(ip_adr=line1[0], 
    #                                 date_request=line1[1],
    #                                 safari=line1[2],
    #                                 firefox=line1[3],
    #                                 unrefined_string=line1[4])
    rqsts = Userrequests.objects.all()
    all_req = Userrequests.objects.count()
    

    context = {'Userrequests': rqsts, 'all_req': all_req}  
    return render(request, template_name="testapp/test.html", context=context)