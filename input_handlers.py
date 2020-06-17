import tcod.event

from actions import Action, ActionType

'''handle_keys will only accept one argument, the key
that was pressed. That key press has two options, an action
as defined in the action.py file or None'''


def handle_keys(key) -> [Action, None]:
    action: [Action, None] = None

    # Movement Keys
    if key == tcod.event.K_UP:
        action = Action(ActionType.MOVEMENT, dx=0, dy=-1)
    elif key == tcod.event.K_DOWN:
        action = Action(ActionType.MOVEMENT, dx=0, dy=1)
    elif key == tcod.event.K_LEFT:
        action = Action(ActionType.MOVEMENT, dx=-1, dy=0)
    elif key == tcod.event.K_RIGHT:
        action = Action(ActionType.MOVEMENT, dx=1, dy=0)
    elif key == tcod.event.K_y:
        action = Action(ActionType.MOVEMENT, dx=-1, dy=-1)
    elif key == tcod.event.K_u:
        action = Action(ActionType.MOVEMENT, dx=1, dy=-1)
    elif key == tcod.event.K_b:
        action = Action(ActionType.MOVEMENT, dx=-1, dy=1)
    elif key == tcod.event.K_n:
        action = Action(ActionType.MOVEMENT, dx=1, dy=1)

    elif key == tcod.event.K_ESCAPE:
        action = Action(ActionType.ESCAPE)

    # No valid key was pressed
    return action
