from django.contrib import admin
from Mail.models import Person, Adress, Phone

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    pass


class AdresAdmin(admin.ModelAdmin):
    pass


class PhoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Adress, AdresAdmin)
admin.site.register(Phone, PhoneAdmin)