#
# voice-skill-sdk
#
# (C) 2021, Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#

from skill_sdk.responses import (
    ErrorCode,
    ErrorResponse,
)
from skill_sdk import skill


async def test_return_error_response_from_intent_handler():
    @skill.intent_handler("ERROR")
    def return_error_response():
        return ErrorResponse(code=ErrorCode.INTERNAL_ERROR, text="internal error")

    response = skill.test_intent("ERROR")
    assert isinstance(response, ErrorResponse)
    assert response.code == 999
    assert response.text == "internal error"


def test_init():
    er = ErrorResponse(code=999, text="internal error")
    assert er.code == 999
    assert er.text == "internal error"


def test_as_response_400():
    er = ErrorResponse(code=ErrorCode.INVALID_TOKEN, text="invalid token")
    assert er.code == 2
    assert er.text == "invalid token"


def test_as_response_500():
    er = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, text="unhandled exception")
    assert er.code == 999
    assert er.text == "unhandled exception"
