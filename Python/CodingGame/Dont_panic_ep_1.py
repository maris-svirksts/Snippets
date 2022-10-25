# https://www.codingame.com/ide/puzzle/don't-panic-episode-1

def block(clone_pos, exit_pos, direction, action):
    if (clone_pos > exit_pos and direction == 'RIGHT') or (clone_pos < exit_pos and direction == 'LEFT'):
        action = 'BLOCK'

    return action


# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevator = {}

for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevator[elevator_floor]     = elevator_pos

# game loop
while True:
    # cloneFloor: floor of the leading clone
    # clonePos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    # action: WAIT or BLOCK
    
    clone_floor, clone_pos, direction = input().split()

    clone_floor = int(clone_floor)
    clone_pos   = int(clone_pos)
    action      = 'WAIT'

    if clone_pos >= 0:
        if clone_floor == exit_floor:
            action = block(clone_pos, exit_pos, direction, action)
        else:
            action = block(clone_pos, elevator[clone_floor], direction, action)

    print(action)
