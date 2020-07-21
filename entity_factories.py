from entity import Entity

player = Entity(char="@", color=(255, 255, 255), name="Player")

goblin = Entity(char="g", color=(63, 127, 63), name="Goblin", blocks_movement=True)
troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movement=True)
