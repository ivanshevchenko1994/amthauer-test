from django.db.models import Prefetch
from django.http import HttpRequest
from ninja import Router

from config.constants.api_const import HttpStatus
from src.amthauer.models import Component, Session, ParticipantAnswer, Participant, Question, Answer
from src.amthauer.schemas import ComponentSchemaOut, SessionSchemaOut, SessionSchemaIn, ParticipantAnswerSchemaOut, \
    ParticipantAnswerSchemaIn, ParticipantSchemaOut, ParticipantSchemaIn, ScoreResultSchemaOut, ScoreResultSchemaIn
from src.amthauer.services.db_service import create_session, update_session_by_id, create_participant_answer, \
    create_participant, create_score_result, update_participant_by_id, calculate_score_result_for_specific_session
from src.common.schemas.common_schemas import ResponseSchema
from src.security.services.jwt_service import AuthBearer

amthauer_router = Router(tags=['amthauer'])


@amthauer_router.get(
    "/get_test_data",
    response={
        HttpStatus.OK.value: list[ComponentSchemaOut],
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def get_test_data(request: HttpRequest):
    """Get all components and all questions with answer and return single json response"""
    return Component.objects.filter(is_active=True).order_by('order').prefetch_related(
        Prefetch('question_set', queryset=Question.objects.filter(is_active=True).order_by('order').prefetch_related(
            Prefetch('answer_set', queryset=Answer.objects.filter(is_active=True).order_by('order'))
        ))
    )


@amthauer_router.post(
    "/participant/create",
    response={
        HttpStatus.OK.value: ParticipantSchemaOut,
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def create_new_participant(request: HttpRequest, participant_schema: ParticipantSchemaIn):
    """Create new entry"""
    return create_participant(request.auth.id, participant_schema)


@amthauer_router.get(
    "/participant/all",
    response={
        HttpStatus.OK.value: list[ParticipantSchemaOut],
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def get_all_participants(request: HttpRequest):
    """Get all participants"""
    return Participant.objects.filter(user_id=request.auth.id)


@amthauer_router.get(
    "/participant/{participant_id}",
    response={
        HttpStatus.OK.value: ParticipantSchemaOut,
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def get_participant(request: HttpRequest, participant_id: int):
    """Get all participants"""
    return Participant.objects.get(id=participant_id)


@amthauer_router.patch(
    "/participant/update/{participant_id}",
    response={
        HttpStatus.OK.value: SessionSchemaOut,
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
        HttpStatus.NOT_FOUND.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def update_participant_entry(request: HttpRequest, participant_id: int, participant_schema: ParticipantSchemaIn):
    """Update entry"""
    return update_participant_by_id(participant_id, participant_schema)


@amthauer_router.post(
    "/session/create",
    response={
        HttpStatus.OK.value: SessionSchemaOut,
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def create_new_session(request: HttpRequest, session_schema: SessionSchemaIn):
    """Create new entry"""
    return create_session(session_schema)


@amthauer_router.get(
    "/session/all",
    response={
        HttpStatus.OK.value: list[SessionSchemaOut],
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def get_all_session(request: HttpRequest):
    """Get all components and all questions with answer and return single json response"""
    return Session.objects.filter(participant__user_id=request.auth.id)


@amthauer_router.patch(
    "/session/update/{session_id}",
    response={
        HttpStatus.OK.value: SessionSchemaOut,
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
        HttpStatus.NOT_FOUND.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def update_session_entry(request: HttpRequest, session_id: int, session_schema: SessionSchemaIn):
    """Update entry"""
    return update_session_by_id(session_id, session_schema)


@amthauer_router.post(
    "/participant_answer/create",
    response={
        HttpStatus.OK.value: ParticipantAnswerSchemaOut,
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def create_new_participant_answer(request: HttpRequest, participant_answer_schema: ParticipantAnswerSchemaIn):
    """Create new entry"""
    return create_participant_answer(participant_answer_schema)


@amthauer_router.get(
    "/get_participant_answers/{session_id}",
    response={
        HttpStatus.OK.value: list[ParticipantAnswerSchemaOut],
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def get_participant_answers(request: HttpRequest, session_id: int):
    """Show all entries"""
    return ParticipantAnswer.objects.filter(session_id=session_id)


@amthauer_router.post(
    "/score_result/create",
    response={
        HttpStatus.OK.value: ScoreResultSchemaOut,
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def create_new_score_result(request: HttpRequest, score_result_schema: ScoreResultSchemaIn):
    """Create new entry"""
    return create_score_result(score_result_schema)


@amthauer_router.get(
    "/score_result/calculate_score_result/{session_id}",
    response={
        HttpStatus.OK.value: ScoreResultSchemaOut,
        HttpStatus.BAD_REQUEST.value: ResponseSchema,
    },
    auth=AuthBearer(),
)
def calculate_score_result(request: HttpRequest, session_id: int):
    """Create new entry"""
    return calculate_score_result_for_specific_session(session_id)
