from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import Group
from .models import RevportalUser, RevportalUserAuthentication
from .forms import EditRevportalUserForm, CreateRevportalUserForm


admin.site.unregister(Group)
admin.site.register(RevportalUserAuthentication)


@admin.register(RevportalUser)
class RevportalUserAdmin(UserAdmin):
    
    form = EditRevportalUserForm
    add_form = CreateRevportalUserForm

    list_display = ('email_address', 'username', 'date_of_birth', 'is_superuser', 'is_verified')
    list_filter = ('is_verified', 'is_superuser')

    fieldsets = (
        ('Personal Info', {
            'classes': ('collapse', 'extrapretty'),
            'fields': (('email_address', 'username'), ('first_name', 'middle_name', 'last_name'), ('date_of_birth',),'password'),
            'description': 'Main user details! '
            }),
        ('Permissions', {
            'classes': ('collapse', 'extrapretty'),
            'fields': (('is_active', 'is_superuser', 'is_verified',),),
            'description': 'Key permissions!'
            }),
        ('Logs', {
            'classes': ('collapse', 'extrapretty'),
            'fields': (('created_at', 'updated_at',),),
            'description': 'All logging data from a user! '
            }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (('email_address', 'username'), 'date_of_birth', ('first_name', 'middle_name', 'last_name'), ('password', 'confirm_password')),
        }),
    )

    search_fields = ('email_address','username',)
    ordering = ('email_address',)
    filter_horizontal = ()
    readonly_fields = ['user_id', 'created_at', 'updated_at']

