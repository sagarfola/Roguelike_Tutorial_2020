import tcod.event

from actions import Action, ActionType

'''handle_keys will only accept one argument, the key
that was pressed. That key press has two options, an action
as defined in the action.py file or None'''


def handle_keys(key) -> [Action, None]:
    action: [Action, None] = None

    # Movement Keys
    if key == tcod.event.K_UP or key == tcod.event.K_KP_8:
        action = Action(ActionType.MOVEMENT, dx=0, dy=-1)
    elif key == tcod.event.K_DOWN or key == tcod.event.K_KP_2:
        action = Action(ActionType.MOVEMENT, dx=0, dy=1)
    elif key == tcod.event.K_LEFT or key == tcod.event.K_KP_4:
        action = Action(ActionType.MOVEMENT, dx=-1, dy=0)
    elif key == tcod.event.K_RIGHT or key == tcod.event.K_KP_6:
        action = Action(ActionType.MOVEMENT, dx=1, dy=0)
    elif key == tcod.event.K_y or key == tcod.event.K_KP_7:
        action = Action(ActionType.MOVEMENT, dx=-1, dy=-1)
    elif key == tcod.event.K_u or key == tcod.event.K_KP_9:
        action = Action(ActionType.MOVEMENT, dx=1, dy=-1)
    elif key == tcod.event.K_b or key == tcod.event.K_KP_1:
        action = Action(ActionType.MOVEMENT, dx=-1, dy=1)
    elif key == tcod.event.K_n or key == tcod.event.K_KP_3:
        action = Action(ActionType.MOVEMENT, dx=1, dy=1)

    elif key == tcod.event.K_ESCAPE:
        action = Action(ActionType.ESCAPE)

    # No valid key was pressed
    return action
