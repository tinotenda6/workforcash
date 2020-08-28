from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm
from .models import CustomUser
from .models import ParentProfile, ChildProfile

class CustomUserAdmin(UserAdmin):
#     exclude = ('username',)
    add_form = UserRegisterForm
    ordering =('username',)
    model = CustomUser
    list_display = ['username','email','first_name','last_name','phone_number','is_child','is_guardian_or_parent',]
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','phone_number','is_child','is_guardian_or_parent',)}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2','first_name','last_name','phone_number','is_child','is_guardian_or_parent',)}
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ParentProfile)
admin.site.register(ChildProfile)
