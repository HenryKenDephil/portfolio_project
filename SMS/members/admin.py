from django.contrib import admin
from.models import Member

# Register your models here.

#admin.site.register(Member)

admin.site.site_header = 'SACCO MANAGEMENT SYSTEM(SMS)'
admin.site.site_title = 'Welcome to SMS Demo'
admin.site.index_title = 'Admin Portal'

class AdminMember(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'gender', 'phone', 'email', 'occupation', 'contributions']
    list_display_links = ['id']
    list_per_page = 10
    search_fields = ['name', 'phone', 'email', 'occupation']
    list_filter = ['gender', 'occupation']

    class Meta:
        model = Member

admin.site.register(Member, AdminMember)