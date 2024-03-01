from django.contrib import admin

from .models import UserProfiles, UserPersona, UserInterest

admin.site.register(UserProfiles)
admin.site.register(UserPersona)
admin.site.register(UserInterest)
