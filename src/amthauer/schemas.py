from ninja import ModelSchema, Field, Schema

from src.amthauer.models import Answer, Component, Question, Participant, Session, ParticipantAnswer, ScoreResult


class AnswerSchemaBase(ModelSchema):
    class Config:
        model = Answer
        model_fields = ['question', 'answer_text', 'is_correct', 'order', 'is_active']


class AnswerSchemaOut(AnswerSchemaBase):
    id: int


class QuestionSchemaBase(ModelSchema):
    class Config:
        model = Question
        model_fields = ['component', 'question_text', 'difficulty_level', 'order', 'is_active']


class QuestionSchemaOut(QuestionSchemaBase):
    answers: list[AnswerSchemaOut] = Field(..., alias='answer_set')
    id: int


class ComponentSchemaBase(ModelSchema):
    class Config:
        model = Component
        model_fields = ['component_name', 'component_description', 'component_title', 'order', 'is_active']


class ComponentSchemaOut(ComponentSchemaBase):
    questions: list[QuestionSchemaOut] = Field(..., alias='question_set')
    id: int


class ScoreResultSchemaBase(ModelSchema):
    class Config:
        model = ScoreResult
        model_fields = ['session', 'raw_score', 'standardized_score', 'percentile_rank', 'time_taken_seconds']


class ScoreResultSchemaOut(ScoreResultSchemaBase):
    id: int


class ScoreResultSchemaIn(ScoreResultSchemaBase):
    """Schema In"""


class SessionSchemaBase(ModelSchema):
    class Config:
        model = Session
        model_fields = ['participant', 'title', 'test_date', 'ip_address', 'test_location', 'start_time', 'end_time']


class SessionSchemaOut(SessionSchemaBase):
    id: int
    score_result: ScoreResultSchemaOut | None

    @staticmethod
    def resolve_score_result(obj):
        if hasattr(obj, 'score_result'):
            return obj.score_result
        return None


class SessionSchemaIn(SessionSchemaBase):
    """Schema In"""


class ParticipantSchemaBase(ModelSchema):
    class Config:
        model = Participant
        model_fields = ['user', 'first_name', 'last_name', 'gender', 'date_of_birth', 'email', 'phone_number']


class ParticipantSchemaOut(ParticipantSchemaBase):
    id: int
    session: SessionSchemaOut | None

    @staticmethod
    def resolve_session(obj):
        if hasattr(obj, 'session'):
            return obj.session
        return None


class ParticipantSchemaIn(ParticipantSchemaBase):
    """Schema In"""


class ParticipantAnswerSchemaBase(ModelSchema):
    class Config:
        model = ParticipantAnswer
        model_fields = ['session', 'component', 'question', 'answer', 'time_taken_answer_seconds']


class ParticipantAnswerSchemaOut(ParticipantAnswerSchemaBase):
    id: int


class ParticipantAnswerSchemaIn(ParticipantAnswerSchemaBase):
    """Schema In"""
