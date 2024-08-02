from django.contrib import admin
from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display=['fullname','email','phone','message']

admin.site.register(Contact, ContactAdmin)
# Register your models here.
