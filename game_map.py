import numpy as np  # type: ignore
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        # assigns the width and height values in one line
        self.width, self.height = width, height

        # Creates a 2D array
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F")

        # Creates a small room
        self.tiles[30:33, 22] = tile_types.wall

    # Keeps players inside the map
    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0<= x < self.width and 0 <= y < self.height

    # renders the map
    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]

