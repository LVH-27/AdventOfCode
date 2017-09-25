
def changeDirection(newDirection):
	global currDirection
	if newDirection == 'R':
		currDirection = (currDirection + 1) % 4
	else:
		currDirection = (currDirection - 1) % 4

def move(movement):
	global currDirection
	global horDist
	global verDist
	global first
	newDirection, diiistance = movement[0], int(movement[1:])
	changeDirection(newDirection)

	for distance in range(1, diiistance+1):
		if currDirection == 0:
			verDist += 1
		elif currDirection == 1:
			horDist += 1
		elif currDirection == 2:
			verDist -= 1
		elif currDirection == 3:
			horDist -= 1

		if (horDist, verDist) not in visited:
			visited[(horDist, verDist)] = 1
		elif not first:
			visited[(horDist, verDist)] += 1
			first = True

def getDistanceFromStart(horDist, verDist):
	return abs(horDist) + abs(verDist)



horDist = 0
verDist = 0
currDirection = 0
first = False

visited = {}
visited[(0, 0)] = 1

line = input().split(", ")
for movement in line:
	move(movement)
	print(movement, currDirection, horDist, verDist, getDistanceFromStart(horDist, verDist))

for tup in visited:
	if visited[tup] != 1:
		print(getDistanceFromStart(tup[0], tup[1]))
