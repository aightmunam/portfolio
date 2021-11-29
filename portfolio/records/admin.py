"""
Admin for the records app
"""

from django.contrib import admin

from .models import Education, Experience, Project, Skill, Social


@admin.register(Education, Experience, Project, Skill, Social)
class RecordAdmin(admin.ModelAdmin):
    pass
