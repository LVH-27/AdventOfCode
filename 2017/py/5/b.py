steps = 0

with open("in.txt") as f:
	instructions = [int(x) for x in f.read().split("\n")]

	i = 0
	try:
		while True:
			next_instruction = instructions[i]
			#print("Current address: ", i, "\tNext address: ", instructions[i])
			if next_instruction >= 3:
				instructions[i] -= 1
			else:
				instructions[i] += 1
			i += next_instruction
			steps += 1

	except IndexError as e:
		pass

print(steps)