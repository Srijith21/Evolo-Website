import json

from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Team,Customer,Contact
from web.forms import ContactForm


def index(request):
    teams = Team.objects.all()[:4]
    customers = Customer.objects.all()[:6]

    form= ContactForm()
    
    context={
        "teams" : teams,
        "customers" : customers,
        "form" : form
    }
    return render(request, 'index.html',context=context)

def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()

        response_data={
            "status" : "success",
            "title" : "Registered Correctly",
            "message" : "Subscribed Succesfullly"
        }   
    else:
        response_data={
            "status" : "error",
            "title" : "Already Registered",
            "message" : "Already Subscribed"
        } 
        
        
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")