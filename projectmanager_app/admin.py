from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    pass

@admin.register(Member)
class MemberAdmin(ModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(ModelAdmin):
    pass

@admin.register(Invitation)
class InvitationAdmin(ModelAdmin):
    pass

@admin.register(Discussion)
class DiscussionAdmin(ModelAdmin):
    pass