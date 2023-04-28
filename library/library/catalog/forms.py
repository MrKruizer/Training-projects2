from django.utils.translation import gettext_lazy as gtl
from django.core.exceptions import ValidationError
from django import forms
from .models import *
import datetime

class RenewBookForm(forms.Form):
	renewal_date = forms.DateField(help_text='Between now and 4 weeks(default 3).')

	def clean_renewal_date(self):
		data = self.cleaned_data['renewal_date']

		if data < datetime.date.today():
			raise ValidationError(gtl('Invalid date - renewal in past'))
		if data > datetime.date.today() + datetime.timedelta(weeks=4):
			raise ValidationError(gtl('Invalid date - renewal more than 4 weeks ahead'))

		return data

class RenewBookModelForm(forms.ModelForm):
	class Meta:
		model = BookInstance
		fields = ['due_back']