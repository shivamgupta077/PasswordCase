#username: mayadmin
#password: adminpassword

from django.contrib import admin
from .models import Case, Profile, Question, Passwords

# Register your models here.
admin.site.register(Case)
admin.site.register(Question)
admin.site.register(Passwords)
admin.site.register(Profile)