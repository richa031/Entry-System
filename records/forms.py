from django import forms

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length = 10, min_length = 10)


class VisitForm(forms.Form):
    visitor_name = forms.CharField(max_length=50)
    visitor_number = forms.CharField(max_length = 10, min_length = 10)
    visitor_email = forms.EmailField()
    host_name = forms.CharField(max_length=50)
    host_number = forms.CharField(max_length = 10, min_length = 10)
    host_email = forms.EmailField()


    
