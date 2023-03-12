# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from apps.authentication.models import User

class EmployeeAdmin(UserAdmin):
    pass
admin.site.register(User)