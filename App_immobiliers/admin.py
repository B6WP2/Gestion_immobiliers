from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nom', 'prenom', 'telephone', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'nom', 'prenom', 'telephone')
    ordering = ('-date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)
