import pgzrun
from pgzhelper import *

# screen = pygame.display.set_mode((800, 600)) # change to the real resolution
# alien = Actor('alien')
# alien.flip_x = True

# def draw():
#   alien.draw()


TILE_SIZE = 64
WIDTH = TILE_SIZE * 8
HEIGHT = TILE_SIZE * 8

tiles = ['empty', 'wall', 'goal']

# maze = [
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1],
#     [1, 0, 1, 0, 1, 0, 1, 1],
#     [1, 0, 1, 0, 0, 2, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1]
# ]

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]


player = Actor("tod", anchor=(0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))
enemy = Actor("enemy", anchor=(0, 0), pos=(3 * TILE_SIZE, 6 * TILE_SIZE))
enemy.yv = -1


def draw():
    screen.clear()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x, y))
    player.draw()
    enemy.draw()

def on_key_down(key):
    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if key == keys.UP:
        row = row - 1
    if key == keys.DOWN:
        row = row + 1
    if key == keys.LEFT:
        column = column - 1
    if key == keys.RIGHT:
        column = column + 1
    # player.x = column * TILE_SIZE
    # player.y = row * TILE_SIZE

    tile = tiles[maze[row][column]]
    if tile == 'empty':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration=0.1, pos=(x, y))
    elif tile == 'goal':
        print("Well done")
        exit()


    # enemy movement
    row = int(enemy.y / TILE_SIZE)
    column = int(enemy.x / TILE_SIZE)
    row = row + enemy.yv
    tile = tiles[maze[row][column]]
    if not tile == 'wall':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy, duration=0.1, pos=(x, y))
    else:
        enemy.yv = enemy.yv * -1
    if enemy.colliderect(player):
        print("You died")
        exit()

pgzrun.go()
