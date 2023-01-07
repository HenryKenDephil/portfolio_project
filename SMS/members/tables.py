import django_tables2 as tables
from .models import Members

class MembersTable(tables.Table):
    
    class Meta:
        model = Members
        fields = ('id', 'first_name', 'last_name', 'gender', 
                    'date', 'phone', 'email', 'occupation', 'contributions')
        
