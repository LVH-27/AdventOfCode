# sector = int(input())
sector = 5  # 325489

direction = 0  # 0 - RIGHT, 1 - UP, 2 - LEFT, 3 - DOWN
step_size = 1  # step size for a given spiral direction iteration

steps = {0: 0, 1: 0, 2: 0, 3: 0}
decrement = False

done = False

man_dist = 0

def change_direction():
	global direction
	global step_size
	global decrement

	direction = (direction + 1) % 4
	if direction % 2 == 0:
		step_size += 1

	if direction > 1:
		decrement = True
	else:
		decrement = False



for i in range(sector):

	if sector - i > step_size:  # granulation control
		steps[direction] += step_size if not decrement else -step_size
		i += step_size - 1

	else:
		for j in range(step_size):
			if i == sector - 1:
				done = True
				break
			steps[direction] += 1 if not decrement else -1
			i += 1

	if done:
		break
	#print(steps)
	change_direction()

print("Moves right: ", steps[0])
print("Moves up: ", steps[1])
print("Moves left: ", steps[2])
print("Moves down: ", steps[3])
print()
print("Manhattan distance: ", abs(steps[0] + steps[2]) + abs(steps[1] + steps[3]))