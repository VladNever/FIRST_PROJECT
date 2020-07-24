from django.shortcuts import render
from django.http import HttpResponse
import requests



def rates(request):

    currencies = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0')
    currencies = currencies.json()

    usd = currencies[4].get('Cur_OfficialRate')
    eur = currencies[5].get('Cur_OfficialRate')
    rub = currencies[16].get('Cur_OfficialRate')
    
    context = {'usd': usd, 'eur': eur, 'rub': rub, 'value1': 'значение'}
    return render(request, template_name="books/list_books.html", context=context)
