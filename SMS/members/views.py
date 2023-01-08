from django.shortcuts import render, get_object_or_404, redirect
from.models import Members
from django.http import HttpResponse
from django_tables2 import RequestConfig
from .forms import MemberForm, EditForm
from django.contrib import messages
from .tables import MembersTable
from django.core.paginator import Paginator
from django.db.models import Q
from django.template.context_processors import csrf

def home(request):
    return render(request, 'members/home.html')

def members(request):
    members = Members.objects.all().order_by()
    '''adding django table module'''
    membbers_table = MembersTable(members)
    RequestConfig(request, paginate={'per_page':5}).configure(membbers_table)

    '''adding members table pagination module'''
    paginator = Paginator(members, 6)
    page_number = request.GET.get('page')
    paginator_module = paginator.get_page(page_number)
    '''dictionary of items to bbe shown in the members_list.html'''
    args = {'members':members, 'members_table':membbers_table, 'paginator_module':paginator_module}
    return render(request,'members/members_list.html', args) 
    

def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member=form.save()
            messages.add_message(request, messages.SUCCESS, 'Member created successfully')
            return redirect('members')
        else:
            args = {'form':form}
            return render(request,'members/create_member.html', args)
    else:
        form = MemberForm()
    args = {'form': form}
    args.update(csrf(request))
    return render(request,'members/create_member.html', args)

        
'''def edit_member(request, id):
    member = get_object_or_404(Members, id=id)
    return render(request,'members/edit_member.html', {'member': member})'''

def edit_member(request, id):
    member = get_object_or_404(Members, id=id)
    form = EditForm(request.POST or None, instance = member)
    if form.is_valid():
        form.save()
        return redirect('members') 

    form = EditForm()
    context ={
        'member': member
    }
    return render(request,'members/edit_member.html', {'member': context})

def delete_member(request, id):
    member = get_object_or_404(Members, id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('delete')
    return render(request, 'members/delete_member.html', {'member': member})



def search_members(request):
    search_keyword = request.GET['member_search']
    if search_keyword != '':
        searched_queryset = Members.objects.all().filter(
        Q(name__icontains=search_keyword) | Q(email__icontains=search_keyword) | Q(gender__iexact=search_keyword) |
        Q(phone_number__icontains=search_keyword) | Q(occupation__icontains=search_keyword)| Q(balance__icontains=search_keyword) |
        Q(occupation__iexact=search_keyword) | Q(id__iexact=search_keyword) 
        ).order_by()

        paginator = Paginator(searched_queryset,5)
        page_number = request.GET.get('page')
        paginator_module = paginator.get_page(page_number)
        args = {'paginator_module':paginator_module,'search_keyword':search_keyword}
        return render(request,'members/members_list.html',args)
    else:
        return redirect('members/members_list.html')

        
        