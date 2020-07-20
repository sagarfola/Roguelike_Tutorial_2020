import tcod
import copy
from engine import Engine
import entity_factories
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    # Variables for screen dimensions
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    # Sets the custom font based on the file
    tileset = tcod.tileset.load_tilesheet("data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    # Use this variable to accept and process events
    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player
    )

    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

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
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


# When you run the script, it will run everything based on the
#   main function. This is useful when having several files
#   or programs that feed into a main function to ensure
#   the right parts of the program are run from the right place.
if __name__ == "__main__":
    main()
