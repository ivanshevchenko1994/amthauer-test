from django.db.models import QuerySet

from config.constants.api_const import HttpStatus, ErrorKeys, ErrorResponse
from src.account.value_objects import UserId
from src.amthauer.models import Component, Session, ParticipantAnswer, Participant, ScoreResult
from src.amthauer.schemas import SessionSchemaIn, ParticipantAnswerSchemaIn, ParticipantSchemaIn
from src.common.schemas.common_schemas import ResponseSchema


def create_session(session: SessionSchemaIn) -> tuple[
                                                    int, QuerySet | Session] | \
                                                tuple[int, ResponseSchema]:

    try:
        new_session: QuerySet | Session = Session(
            participant_id=session.participant,
            test_date=session.test_date,
            test_location=session.test_location,
            start_time=session.start_time,
            end_time=session.end_time,
        )
        new_session.save()
        print('------------------------------')
        print(new_session)
        print('------------------------------')
        return HttpStatus.OK.value, new_session
    except Exception as e:
        print(e)
        return HttpStatus.BAD_REQUEST.value, ResponseSchema(
            **{ErrorKeys.MESSAGE.value: ErrorResponse.CREATE_NEW_DB_ENTRY_ERROR.value}
        )


def update_session_by_id(session_id: int, session_schema: SessionSchemaIn) -> tuple[
                                                                                     int, QuerySet | Session] | \
                                                                                 tuple[int, ResponseSchema]:
    try:
        existed_session: QuerySet | Session = Session.objects.get(id=session_id)
        for attr, value in session_schema.dict(exclude_unset=True).items():
            setattr(existed_session, attr, value)
        existed_session.save()
        return HttpStatus.OK.value, existed_session
    except Session.DoesNotExist as e:
        print(e)
        return HttpStatus.NOT_FOUND.value, ResponseSchema(
            **{ErrorKeys.MESSAGE.value: ErrorResponse.NOT_EXISTING_DB_ENTRY_ERROR.value}
        )
    except Exception as e:
        print(e)
        return HttpStatus.BAD_REQUEST.value, ResponseSchema(
            **{ErrorKeys.MESSAGE.value: ErrorResponse.SHOW_ONE_DB_ENTRY_ERROR.value}
        )


def create_participant_answer(participant_answer_schema: ParticipantAnswerSchemaIn) -> tuple[
                                                    int, QuerySet | ParticipantAnswer] | \
                                                tuple[int, ResponseSchema]:
    try:
        new_participant_answer: QuerySet | ParticipantAnswer = ParticipantAnswer(
            session_id=participant_answer_schema.session,
            component_id=participant_answer_schema.component,
            question_id=participant_answer_schema.question,
            answer_id=participant_answer_schema.answer,
            time_taken_answer_seconds=participant_answer_schema.time_taken_answer_seconds,
        )
        new_participant_answer.save()
        print('------------------------------')
        print(new_participant_answer)
        print('------------------------------')
        return HttpStatus.OK.value, new_participant_answer
    except Exception as e:
        print(e)
        return HttpStatus.BAD_REQUEST.value, ResponseSchema(
            **{ErrorKeys.MESSAGE.value: ErrorResponse.CREATE_NEW_DB_ENTRY_ERROR.value}
        )


def create_participant(user_id: UserId, participant_schema: ParticipantSchemaIn) -> tuple[
                                                    int, QuerySet | Participant] | \
                                                tuple[int, ResponseSchema]:
    try:
        new_participant: QuerySet | Participant = Participant(
            user_id=user_id,
            first_name=participant_schema.first_name,
            last_name=participant_schema.last_name,
            gender=participant_schema.gender,
            date_of_birth=participant_schema.date_of_birth,
            email=participant_schema.email,
            phone_number=participant_schema.phone_number
        )
        new_participant.save()
        print('------------------------------')
        print(new_participant)
        print('------------------------------')
        return HttpStatus.OK.value, new_participant
    except Exception as e:
        print(e)
        return HttpStatus.BAD_REQUEST.value, ResponseSchema(
            **{ErrorKeys.MESSAGE.value: ErrorResponse.CREATE_NEW_DB_ENTRY_ERROR.value}
        )


def create_score_result(score_result_schema: ParticipantSchemaIn) -> tuple[
                                                    int, QuerySet | ScoreResult] | \
                                                tuple[int, ResponseSchema]:
    try:
        new_score_result: QuerySet | ScoreResult = ScoreResult(
            session_id=score_result_schema.session,
            raw_score=score_result_schema.raw_score,
            standardized_score=score_result_schema.standardized_score,
            percentile_rank=score_result_schema.percentile_rank,
            time_taken_seconds=score_result_schema.time_taken_seconds,
        )
        new_score_result.save()
        print('------------------------------')
        print(new_score_result)
        print('------------------------------')
        return HttpStatus.OK.value, new_score_result
    except Exception as e:
        print(e)
        return HttpStatus.BAD_REQUEST.value, ResponseSchema(
            **{ErrorKeys.MESSAGE.value: ErrorResponse.CREATE_NEW_DB_ENTRY_ERROR.value}
        )


def update_participant_by_id(participant_id: int, participant_schema: ParticipantSchemaIn) -> tuple[
                                                                                     int, QuerySet | Participant] | \
                                                                                 tuple[int, ResponseSchema]:
    try:
        existed_participant: QuerySet | Participant = Participant.objects.get(id=participant_id)
        for attr, value in participant_schema.dict(exclude_unset=True).items():
            setattr(existed_participant, attr, value)
        existed_participant.save()
        return HttpStatus.OK.value, existed_participant
    except Session.DoesNotExist as e:
        print(e)
        return HttpStatus.NOT_FOUND.value, ResponseSchema(
            **{ErrorKeys.MESSAGE.value: ErrorResponse.NOT_EXISTING_DB_ENTRY_ERROR.value}
        )
    except Exception as e:
        print(e)
        return HttpStatus.BAD_REQUEST.value, ResponseSchema(
            **{ErrorKeys.MESSAGE.value: ErrorResponse.SHOW_ONE_DB_ENTRY_ERROR.value}
        )
