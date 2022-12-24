from django.http import HttpResponse
from django.shortcuts import render, redirect



def home(request):
    #return HttpResponse("welcome to sms.com")
    return render(request,'home.html')



def loans(request):
    return HttpResponse("Active loans")
    #return render(request,'loans.html')

def accounts(request):
    return HttpResponse("loan payments status")
    #return render(request,'accounts.html') uncomment and remove 
    # httpresponse after developing loan.html