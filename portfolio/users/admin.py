from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from portfolio.records.models import Education, Experience, PersonalInfo, Social
from portfolio.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


class PersonalInfoInline(admin.StackedInline):
    model = PersonalInfo


class ExperiencesInline(admin.TabularInline):
    model = Experience


class EducationsInline(admin.TabularInline):
    model = Education


class SocialsInline(admin.TabularInline):
    model = Social
    fields = ["title", "profile_link"]


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "email", "first_name", "is_superuser"]
    search_fields = ["name"]
    inlines = [EducationsInline, ExperiencesInline, SocialsInline]
