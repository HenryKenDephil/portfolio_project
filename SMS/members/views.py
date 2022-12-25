from django.shortcuts import render
from.models import Member
from django.http import HttpResponse
from tables import MemberTable
from django_tables2 import RequestConfig


def members(request):
    members = Member.objects.all().order_by()
    return render(request,'members/members_list.html', {'members': members}) 
    

def member_details(request):
    #member_id = request.GET.get('id')
    #member = Member.objects.get(id=member_id)
    #return render(request,'members/member_details.html', {'member': member})
    return HttpResponse
