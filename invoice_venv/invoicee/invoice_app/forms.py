from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Client, Product, Invoice, Settings
import json


#form for DateInput
class DateInput(forms.DateInput):
    input_type = 'date'


# form for UserLogin
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


# form for Client
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['clientName','addressLine1', 'province', 'postalCode', 'phoneNumber', 'emailAddress']


# form for Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','discription','quantity','price','currency']



# form for Invoice
class InvoiceForm(forms.ModelForm):
    dueDate = forms.DateField(
        required = True,
        label = 'Invoice Due',
        widget = DateInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Invoice
        fields = ['title','number','dueDate','paymentTerms','status','notes']

# form for Settings
class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['clientName','addressLine1','province','postalCode','phoneNumber','emailAddress']
