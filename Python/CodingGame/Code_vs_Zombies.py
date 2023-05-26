# https://www.codingame.com/ide/puzzle/code-vs-zombies

import math

class Human:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

class Zombie:
    def __init__(self, id, x, y, nextX, nextY):
        self.id = id
        self.x = x
        self.y = y
        self.nextX = nextX
        self.nextY = nextY

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# game loop
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    humans = []
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append(Human(human_id, human_x, human_y))

    zombie_count = int(input())
    zombies = []
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies.append(Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext))

    # Find the closest zombie to a human
    min_distance = float('inf')
    target_x, target_y = 0, 0
    for human in humans:
        for zombie in zombies:
            dist = distance(human.x, human.y, zombie.nextX, zombie.nextY)
            if dist < min_distance:
                min_distance = dist
                target_x = zombie.x
                target_y = zombie.y

    # Go to the closest zombie
    print(f"{target_x} {target_y}")
