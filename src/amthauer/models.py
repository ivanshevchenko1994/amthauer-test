from django.db import models

from config.constants.model_const import GenderChoices
from src.account.models import User
from src.common.mixins.models.date_time_mixin import DateTimeMixin


# Create your models here.
class Participant(DateTimeMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_data_collect',
        null=True,
    )  # FK to user
    first_name = models.CharField(max_length=255, null=True, db_index=True)
    last_name = models.CharField(max_length=255, null=True, db_index=True)
    gender = models.IntegerField(choices=[(choice.value, choice.name) for choice in GenderChoices])
    date_of_birth = models.DateField()
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        managed = True
        db_table = "participant"
        verbose_name = "Participant"
        verbose_name_plural = "Participants"


class Session(DateTimeMixin):
    participant = models.OneToOneField(
        Participant,
        on_delete=models.CASCADE,
        null=True,
        related_name='session'
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    test_date = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    test_location = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.participant} {self.test_date}'

    class Meta:
        managed = True
        db_table = "session"
        verbose_name = "Session"
        verbose_name_plural = "Sessions"


class Component(DateTimeMixin):
    component_name = models.CharField(max_length=255)
    component_description = models.TextField(null=True, blank=True)
    component_title = models.CharField(max_length=255)
    order = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.component_name}'

    class Meta:
        managed = True
        db_table = "component"
        verbose_name = "Component"
        verbose_name_plural = "Components"


# class Section(models.Model):
#     component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True)
#     section_name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f'{self.component} - {self.section_name}'
#
#     class Meta:
#         managed = True
#         db_table = "section"
#         verbose_name = "Section"
#         verbose_name_plural = "Sections"


class Question(DateTimeMixin):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True)
    question_text = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    difficulty_level = models.IntegerField(null=True, default=1)
    dependent_question = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    order = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.component} - {self.question_text}'

    class Meta:
        managed = True
        db_table = "question"
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Answer(DateTimeMixin):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer_text = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    order = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.question} - {self.answer_text}'

    class Meta:
        managed = True
        db_table = "answer"
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


class ParticipantAnswer(DateTimeMixin):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    time_taken_answer_seconds = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.session}'

    class Meta:
        managed = True
        db_table = "participant_answer"
        verbose_name = "Participant answer"
        verbose_name_plural = "Participant answers"


class ScoreResult(DateTimeMixin):
    session = models.OneToOneField(
        Session,
        on_delete=models.CASCADE,
        null=True,
        related_name='score_result'
        )
    raw_score = models.IntegerField(null=True, blank=True)
    standardized_score = models.FloatField(null=True, blank=True)
    percentile_rank = models.FloatField(null=True, blank=True)
    time_taken_seconds = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.session}'

    class Meta:
        managed = True
        db_table = "score_result"
        verbose_name = "Score result"
        verbose_name_plural = "Score results"
