from django.contrib import admin
from contactform.models import Contactform
class contactformAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','subject','message')

admin.site.register(Contactform,contactformAdmin)
# Register your models here.
