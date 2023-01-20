from django import forms 
from .models import Members

#form to creating new memebers
class MemberForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = "__all__"

class EditForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = "__all__"
