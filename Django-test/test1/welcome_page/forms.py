from django import forms

class UserForm(forms.Form):
	name = forms.CharField(strip=True, required=True, min_length=2)
	age = forms.IntegerField(min_value=18, max_value=111, initial=18, required=True)
	password = forms.CharField(strip=True,widget=forms.PasswordInput(), required=True, min_length=4)