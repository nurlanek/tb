from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# UserAdmin'i genişletin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'list_groups')

    # Kullanıcının gruplarını gösteren bir metot tanımlayın
    def list_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    list_groups.short_description = 'Groups'

# Admin panelinde UserAdmin'i özelleştirilmiş versiyonuyla yeniden kaydedin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
