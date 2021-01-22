from django import forms
from .models import Adress, Person

choices = (
        ('private', 'Private'),
        ('bussines', 'bussines')

    )
delete = (
    'YES', 'NO'
)

class PersonForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=35, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(label='Last name', max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your last name'}))
    description = forms.CharField(label='Description', max_length=300, widget=forms.TextInput(
        attrs={'placeholder': 'Add description'}))
    adress = forms.ModelChoiceField(queryset=Adress.objects.all())


class AdressForm(forms.Form):
    town = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'placeholder': 'Town'}))
    street = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Street'}))
    home_number = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Home number'}))
    flat_number = forms.IntegerField()
    post_code = forms.CharField(max_length=7, widget=forms.TextInput(
        attrs={'placeholder': 'Post code'}))


class PhoneForm(forms.Form):
    number = forms.IntegerField()
    type = forms.ChoiceField(choices=choices)


class EmailForm(forms.Form):
    email_adress = forms.EmailField()
    type = forms.ChoiceField(choices=choices)


class DeleteConfirmation(forms.Form):
    delete = forms.BooleanField()


class EditForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=35, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(label='Last name', max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your last name'}))
    description = forms.CharField(label='Description', max_length=300, widget=forms.TextInput(
        attrs={'placeholder': 'Add description'}))

class AddGroup(forms.Form):
    name = forms.CharField(max_length=40)


class addPersonToGroupForm(forms.Form):
    persons = forms.ModelMultipleChoiceField(queryset=Person.objects.all())