from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from src.amthauer.models import Participant, Session, Component, Question, Answer, ParticipantAnswer, ScoreResult


class SessionDataInline(admin.TabularInline):
    model = Session
    extra = 0


class QuestionDataInline(admin.TabularInline):
    model = Question
    extra = 0


class AnswerDataInline(admin.TabularInline):
    model = Answer
    extra = 0


class ScoreResultDataInline(admin.TabularInline):
    model = ScoreResult
    extra = 0


class ComponentForm(forms.ModelForm):
    component_description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Component
        fields = '__all__'


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "first_name", "last_name", "gender", "date_of_birth", "email", "created_at", "updated_at")
    search_fields = ("id", "first_name", "last_name", "gender", "date_of_birth", "email")
    inlines = (SessionDataInline,)
    ordering = ("id",)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("id", "participant", 'title', 'ip_address', "test_date", "test_location", "start_time", "end_time",
                    "created_at", "updated_at")
    search_fields = ("id", "participant__first_name", "participant__last_name")
    inlines = (ScoreResultDataInline,)
    ordering = ("id",)


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    form = ComponentForm
    list_display = (
        "id", "component_name", "component_description", "component_title", "order", "is_active", "created_at",
        "updated_at")
    search_fields = ("id", "component_name", "component_description", "component_title")
    inlines = (QuestionDataInline,)
    ordering = ("id",)


# @admin.register(Component)
# class ComponentAdmin(admin.ModelAdmin):
#     list_display = (
#         "id", "component_name", "component_description", "component_title", "order", "is_active", "created_at",
#         "updated_at")
#     search_fields = ("id", "component_name", "component_description", "component_title")
#     inlines = (QuestionDataInline,)
#     ordering = ("id",)


# @admin.register(Section)
# class SectionAdmin(admin.ModelAdmin):
#     list_display = ("id", "component__component_name", "section_name", "created_at", "updated_at")
#     search_fields = ("id", "component__component_name", "section_name")
#     ordering = ("id",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "component", "question_text", "description", "difficulty_level", "dependent_question",
                    "order", "is_active", "created_at", "updated_at")
    search_fields = ("id", "component__component_name", "question_text")
    list_filter = ("component",)
    inlines = (AnswerDataInline,)
    ordering = ("id",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer_text", "is_correct", "order", "is_active", "created_at", "updated_at")
    search_fields = ("id", "question__question_text", "answer_text")
    ordering = ("id",)


@admin.register(ParticipantAnswer)
class ParticipantAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "id", "session", "component", "question", "answer", "time_taken_answer_seconds", "created_at", "updated_at")
    search_fields = ("id",)
    list_filter = ("component",)
    ordering = ("id",)


@admin.register(ScoreResult)
class ScoreResultAdmin(admin.ModelAdmin):
    list_display = (
        "id", "session", "raw_score", "standardized_score", "percentile_rank", "time_taken_seconds", "created_at",
        "updated_at")
    search_fields = ("id",)
    list_filter = ("session__participant",)
    ordering = ("id",)
