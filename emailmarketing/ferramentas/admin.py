from django.contrib import admin

# Register your models here.
from .models import Campaign, Contact, GroupContacts, EmailContent, Clients

admin.site.register(Campaign)
admin.site.register(Contact)
admin.site.register(GroupContacts)
admin.site.register(EmailContent)
admin.site.register(Clients)