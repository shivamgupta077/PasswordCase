#username: mayadmin
#password: adminpassword

from django.contrib import admin
from .models import Case, Profile, Question

# Register your models here.
admin.site.register(Case)
admin.site.register(Profile)
admin.site.register(Question)