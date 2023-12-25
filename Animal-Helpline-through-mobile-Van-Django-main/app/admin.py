from django.contrib import admin

# Register your models here.
from .models import Contact,dead,harassement,injured,Feedback
admin.site.site_header = 'Animal Helpline Administration'

admin.site.register(Contact)
admin.site.register(dead)
admin.site.register(harassement)
admin.site.register(injured)
admin.site.register(Feedback)