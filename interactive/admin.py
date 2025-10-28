
from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "result", "created_at")
    list_filter = ("result",)
    search_fields = ("name",)
