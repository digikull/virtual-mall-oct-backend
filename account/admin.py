from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea



User = get_user_model()
#Changes in Admin Panel in User Interface
class  UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'full_name',)
    list_filter = ('email', 'full_name', 'is_active', 'is_staff')
    ordering = ('-signup_date',)
    list_display = ('email',  'full_name',
                     'is_staff')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('full_name','password',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    filter_horizontal = ()



admin.site.register(User,  UserAdminConfig)