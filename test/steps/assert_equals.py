from behave import *

from logntime.validation.assertions.assert_equals import assert_equals
from logntime.validation.assertions.transform import bypass


@given("a custom message and to objects that are not equal")
def step_impl(context):
    context.custom_message = "Very important test failed.\n"
    context.expected = (1, 2, 3)
    context.result = (1, 2, 3, 4)
    context.format_data = bypass


@when("assert_equals is executed with the given parameters")
def step_impl(context):
    try:
        assert_equals(
            context.expected,
            context.result,
            custom_message=context.custom_message,
            format_data=context.format_data
        )
    except Exception as exception:
        context.exception = exception


@then("the exception message should start with the custom message")
def step_impl(context):
    assert str(context.exception).startswith("Very important test failed.")


@given("a custom format method and to objects that are not equal")
def step_impl(context):
    context.expected = (1, 2, 3)
    context.result = (5, 6, 7)
    context.custom_message = ""
    context.format_data = lambda d: ">".join(map(str, d))


@then("the parameters in the exception message should be formatted accordingly")
def step_impl(context):
    message = str(context.exception)
    print(message)
    assert "1>2>3" in message
    assert "5>6>7" in message
