from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from Mail.models import Person, Adress, Phone, Email, Group
from Mail.forms import PersonForm, AdressForm, PhoneForm, EmailForm, DeleteConfirmation, EditForm, AddGroup, addPersonToGroupForm


# Create your views here.

class LandingPage(View):

    def get(self, request):
        all_persons = Person.objects.order_by('first_name')
        groups = Group.objects.all()
        ctx = {
            'all_persons': all_persons,
            'groups': groups
        }
        return render(request, 'landingPage.html', ctx)

    def post(self, request):
        pass


class PersonView(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        phones = Phone.objects.filter(person_id=id).values('number', 'type')
        emails = Email.objects.filter(user_id=id).values('email_adress', 'type')
        ctx = {
            'person': person,
            'phones': phones,
            'emails': emails,

        }
        return render(request, 'personPage.html', ctx)


class newPersonView(View):

    def get(self, request):
        form = PersonForm()
        ctx = {
            'form': form
        }
        return render(request, 'newPersonPage.html', ctx)

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            desc = form.cleaned_data['description']
            person = Person(first_name=first_name, last_name=last_name, description=desc)
            person.save()
        return redirect('/')


class addAdressView(View):

    def get(self, request):
        form = AdressForm()
        ctx = {
            'form': form
        }
        return render(request, 'addAdressPage.html', ctx)

    def post(self, request):
        form = AdressForm(request.POST)
        if form.is_valid():
            town = form.cleaned_data['town']
            street = form.cleaned_data['street']
            home_number = form.cleaned_data['home_number']
            flat_number = form.cleaned_data['flat_number']
            post_code = form.cleaned_data['post_code']
            adress = Adress(town=town, street=street, home_number=home_number, flat_number=flat_number,
                            post_code=post_code)
            adress.save()
        return redirect('/')


class addPhoneView(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        form = PhoneForm()
        ctx = {
            'form': form,
            'person': person
        }
        return render(request, 'addPhonePage.html', ctx)

    def post(self, request, id):
        form = PhoneForm(request.POST)
        person = Person.objects.get(pk=id)
        if form.is_valid():
            number = form.cleaned_data['number']
            type = form.cleaned_data['type']
            new_phone = Phone(person=person, number=number, type=type)
            new_phone.save()
        return redirect(f'/person/{id}/')


class addEmailView(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        form = EmailForm()
        ctx = {
            'form': form,
            'person': person
        }
        return render(request, 'addEmailPage.html', ctx)

    def post(self, request, id):
        form = EmailForm(request.POST)
        person = Person.objects.get(pk=id)
        if form.is_valid():
            email_adress = form.cleaned_data['email_adress']
            type = form.cleaned_data['type']
            new_adress = Email(email_adress=email_adress, type=type, user=person)
            new_adress.save()
        return redirect(f'/person/{id}/')


class deletePersonView(View):

    def get(self, request, id):
        form = DeleteConfirmation()
        ctx = {
            'form': form,
        }
        return render(request, 'deletePage.html', ctx)

    def post(self, request, id):
        form = DeleteConfirmation(request.POST)
        if form.is_valid():
            conf = form.cleaned_data['delete']
            if conf:
                Person.objects.filter(pk=id).delete()
            else:
                return redirect(f'/person/{id}/')
        return redirect('/')


class editView(View):

    def get(self, request, id):
        form = EditForm()
        ctx = {
            'form': form
        }
        return render(request, 'editPage.html', ctx)

    def post(self, request, id):
        form = EditForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            desc = form.cleaned_data['description']
            Person.objects.filter(pk=id).update(first_name=first_name, last_name=last_name, description=desc)
        return redirect('/')


class addGroupView(View):

    def get(self, request):
        groups = Group.objects.all()
        form = AddGroup()
        ctx = {
            'form': form,
            'groups': groups
        }
        return render(request, 'addGroupPage.html', ctx)

    def post(self, request):
        form = AddGroup(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_group = Group(name=name)
            new_group.save()
        return redirect('/')


class singleGroupView(View):

    def get(self, request, id):
        group = Group.objects.get(pk=id)
        persons = group.person.all()
        ctx = {
            'group': group,
            'persons': persons
        }
        return render(request, 'singleGroupPage.html', ctx)


class addPersonToGroupView(View):

    def get(self, request, id):
        form = addPersonToGroupForm()
        ctx = {
            'form': form
        }
        return render(request,' addPersonToGroupPage.html', ctx)

    def post(self, request, id):
        form = addPersonToGroupForm(request.POST)
        group = Group.objects.get(pk=id)
        if form.is_valid():
            name = group.name
            persons = form.cleaned_data['persons']
            print(persons)
            for i in range(len(persons)):
                group.person.add(persons[i])
                i+=1
        return redirect('/')

class deletePersonFromGroupView(View):

    def get(self, request, id, id_person):
        group = Group.person.through.objects.filter(person=id_person)
        print(group)
        group.delete()
        return redirect('/')
