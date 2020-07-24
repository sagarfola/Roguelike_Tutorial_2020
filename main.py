import tcod

import copy

import color
from engine import Engine
import entity_factories
from procgen import generate_dungeon


def main() -> None:
    # Variables for screen dimensions
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    # Sets the custom font based on the file
    tileset = tcod.tileset.load_tilesheet("data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )
    engine.update_fov()

    engine.message_log.add_message(
        "Hello and welcome to yet another dungeon!", color.welcome_text
    )

    # This function initializes and creates the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True
    ) as context:
        # Order "F" means coordinates are x, y instead of y, x
        # Creates the console that we will be drawing to
        root_console = tcod.Console(screen_width, screen_height, order="F")
        # This is the game loop!
        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            engine.event_handler.handle_events(context)


# When you run the script, it will run everything based on the
#   main function. This is useful when having several files
#   or programs that feed into a main function to ensure
#   the right parts of the program are run from the right place.
if __name__ == "__main__":
    main()
