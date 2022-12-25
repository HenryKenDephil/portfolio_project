import django_tables2 as tables
from models import Member

class Member(tables.Table):
    
    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'gender', 
                    'date', 'phone', 'email', 'occupation', 'contributions')
        
