from django import forms

class InsertForm(forms.ModelForm):
    
    id = forms.IntegerField(help_text="Enter Row ID number", required=True)
    first_name = forms.CharField(max_length=50, required=True, help_text="Enter First Name")
    last_name = forms.CharField(max_length=50, required=True, help_text="Enter Last Name")
    