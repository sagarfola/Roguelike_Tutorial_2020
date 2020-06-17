from enum import auto, Enum

'''Enums are a set of pre-defined constant values. They
are set ahead of time and won't change while the program is
running.  We use Enums to track the action types

auto() allows you to automatically set the value of the enums
so you don't have to individually increment each value with a
number 1, 2, 3, ... ,n '''


class ActionType(Enum):
    ESCAPE = auto()
    MOVEMENT = auto()


'''Kwargs are an arbitrary arguement and allows for flexibility 
in inputting arguements into the class or function'''


class Action:
    def __init__(self, action_type: ActionType, **kwargs):
        self.action_type: ActionType = action_type
        self.kwargs = kwargs
