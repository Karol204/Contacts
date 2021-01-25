from django.contrib import admin
from django.urls import path
from Mail.views import LandingPage, PersonView, newPersonView, addAdressView, addPhoneView, addEmailView, \
    deletePersonView, editView, addGroupView, singleGroupView, addPersonToGroupView, deletePersonFromGroupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view()),
    path('person/<int:id>/', PersonView.as_view()),
    path('new-person/', newPersonView.as_view()),
    path('add-adress/', addAdressView.as_view()),
    path('person/<int:id>/add-phone/', addPhoneView.as_view()),
    path('person/<int:id>/add-email/', addEmailView.as_view()),
    path('delete/<int:id>/', deletePersonView.as_view()),
    path('edit/<int:id>/', editView.as_view()),
    path('add-group/', addGroupView.as_view()),
    path('group/<int:id>/', singleGroupView.as_view()),
    path('group/<int:id>/add-person/', addPersonToGroupView.as_view()),
    path('delete/<int:id>/<int:id_person>/', deletePersonFromGroupView.as_view())



]
