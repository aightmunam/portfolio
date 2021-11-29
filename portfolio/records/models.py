"""
All the models for the records app
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeFramedModel, TimeStampedModel


class TitleDescriptionMixin(models.Model):
    """
    A Mixin that adds title and description fields to a model
    """

    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True


class LocationMixin(models.Model):
    """
    A mixin that adds location field to a model
    """

    location = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True


class PersonalInfo(LocationMixin, TimeStampedModel):
    """
    Model to represent all the personal information
    """

    user = models.OneToOneField(
        "users.User", on_delete=models.DO_NOTHING, blank=True, null=True
    )

    date_of_birth = models.DateField()
    picture = models.URLField(blank=True)
    about = models.TextField()


class Project(TitleDescriptionMixin, TimeStampedModel, TimeFramedModel):
    """
    Model to represent a project
    """

    site_url = models.URLField(blank=True)
    source_code_url = models.URLField(blank=True)
    skills_utilized = models.ManyToManyField("records.Skill", related_name="projects")
    affiliation = models.ForeignKey("records.Experience", on_delete=models.DO_NOTHING)


class Skill(TitleDescriptionMixin, TimeStampedModel):
    """
    Model to represent a skill
    """

    class ProficiencyLevel(models.TextChoices):
        """
        Different proficiency levels for a skill
        """

        BASIC = "BA", _("Beginner")
        INTERMEDIATE = "IN", _("Intermediate")
        ADVANCED = "AD", _("Advanced")
        EXPERT = "EX", _("EXPERT")

    reference_url = models.URLField(blank=True)
    proficiency_level = models.CharField(
        max_length=2, choices=ProficiencyLevel.choices, default=ProficiencyLevel.BASIC
    )


class Experience(
    TitleDescriptionMixin, LocationMixin, TimeStampedModel, TimeFramedModel
):
    """
    Model to represent work experience
    """

    user = models.ForeignKey(
        "users.User", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    is_remote = models.BooleanField(default=False)
    company_site_url = models.URLField(blank=True)


class Social(TitleDescriptionMixin, TimeStampedModel):
    """
    Model to represent social media plugs
    """

    user = models.ForeignKey(
        "users.User", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    profile_link = models.URLField(blank=True)


class Education(LocationMixin, TimeStampedModel, TimeFramedModel):
    """
    Model to represent education
    """

    class DegreeChoices(models.TextChoices):
        """
        Different degree choices
        """

        SCHOOL = "HS", _("School")
        BACHELORS = "BS", _("Bachelors")
        MASTERS = "MS", _("Masters")
        CERTIFICATION = "CR", _("Certification")

    user = models.ForeignKey(
        "users.User", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    institute = models.CharField(max_length=300)
    degree = models.CharField(
        max_length=2, choices=DegreeChoices.choices, default=DegreeChoices.CERTIFICATION
    )
    summary = models.TextField(blank=True)
