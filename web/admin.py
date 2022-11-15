from django.contrib import admin
from web.models import Team,Customer,Contact


class TeamAdmin(admin.ModelAdmin):
    list_display = ["name","id","job_role"]

admin.site.register(Team,TeamAdmin)

admin.site.register(Customer)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["email","name"]

admin.site.register(Contact,ContactAdmin)
