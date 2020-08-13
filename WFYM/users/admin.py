from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm
from .models import CustomUser
# from .models import Profile

class CustomUserAdmin(UserAdmin):
    exclude = ('username',)
    add_form = UserRegisterForm
    ordering =('email',)
    model = CustomUser
    list_display = ['email','first_name','last_name','phone_number','is_child','is_guardian_or_parent',]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','phone_number','is_child','is_guardian_or_parent',)}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name','last_name','phone_number','is_child','is_guardian_or_parent',)}
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Profile)
