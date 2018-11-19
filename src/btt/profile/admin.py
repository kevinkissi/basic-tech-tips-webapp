from django.contrib import admin
from django.apps import apps


from btt.profile.models import Profile

class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'id', 'dollars_earned')

admin.site.register(Profile, ProfileAdmin)


#profile = apps.get_app_config('profile')
#
#for model_name, model in profile.models.items():
#    admin.site.register(model)
