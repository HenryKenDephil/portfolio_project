from django.shortcuts import render
from.models import Member

def members(request):
    members = Member.objects.all().order_by('member_id')
    return render(request,'members/members.html', {'members': members}) 
    

# Create your views here.
