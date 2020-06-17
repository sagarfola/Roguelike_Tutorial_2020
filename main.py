import tcod

from actions import Action, ActionType
from input_handlers import handle_keys

def main():
    # Variables for screen dimensions
    screen_width: int = 80
    screen_height: int = 50

    # Player coordinate data
    player_x: int = int(screen_width/2)
    player_y: int = int(screen_height/2)

    # Sets the custom font based on the file
    # TODO place file in its own data folder
    tcod.console_set_custom_font("arial10x10.png", tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    # This function initializes and creates the screen
    with tcod.console_init_root(
        w=screen_width,
        h=screen_height,
        title="Yet Another Roguelike Tutorial",
        order="F",  # Allows the order of coordinates to be [x, y] vs [y, x]
        vsync=True
    ) as root_console:
        # This is the game loop!
        while True:
            # Printing a character on the screen at position 1,1
            root_console.print(x=player_x, y=player_y, string="@")

            # Flush updates the screen to print the character
            tcod.console_flush()

            # clears the console to refresh the screeny
            root_console.clear()

            # Allows the program to close gracefully by pressing the red x in the corner
            for event in tcod.event.wait():

                # Quit the game
                if event.type == "QUIT":
                    raise SystemExit()

                # if the event is a keystroke, it will analyze
                # the key stroke and pass the event.sym as the key argument
                if event.type == "KEYDOWN":
                    action: [Action, None] = handle_keys(event.sym)

                    if action is None:
                        continue

                    action_type: ActionType = action.action_type

                    if action_type == ActionType.MOVEMENT:
                        dx: int = action.kwargs.get("dx", 0)
                        dy: int = action.kwargs.get("dy", 0)

                        player_x += dx
                        player_y += dy

                    elif action_type == ActionType.ESCAPE:
                        raise SystemExit()


# When you run the script, it will run everything based on the
#   main function. This is useful when having several files
#   or programs that feed into a main function to ensure
#   the right parts of the program are run from the right place.
if __name__ == "__main__":
    main()
