from calvin.actor.actor import Actor, condition
from calvin.runtime.north.calvin_token import ExceptionToken


class InputDiv(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        dividend : integer
        divisor : integer
    Output :
        result
    """

    def init(self):
        pass

    @condition(action_input=['dividend', 'divisor'], action_output=['result'])
    def divide(self, numerator, denumerator):
        if denumerator != 0:
            result = numerator / denumerator
        else:
            result = ExceptionToken("Division by 0")
        return (result,)

    action_priority = (divide,)