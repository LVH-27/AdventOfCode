with open("in.txt") as f:
	lines = [line.split() for line in f.readlines()]

instructions = []
registers = {}  # register_name-value pairs
for line in lines:
	register = line[0]
	cond_register = line[4]
	instruction = {"register": register,
					"operation": line[1],
					"value": int(line[2]),
					# "cond_register": line[4],
					# "cond_operator": line[5],
					# "cond_value": int(line[6]),
					"condition": "registers['" + line[4] + \
					"'] " + line[5] + " " + line[6],
					}

	if register not in registers:
		registers[register] = 0  # initialize all registers
	if cond_register not in registers:
		registers[cond_register] = 0

	instructions.append(instruction)

max_val_ever_held = 0
for instruction in instructions:
	if eval(instruction['condition']):
		registers[instruction['register']] += instruction['value'] \
			if instruction['operation'] == "inc" else -instruction['value']
		if registers[instruction['register']] > max_val_ever_held:
			max_val_ever_held = registers[instruction['register']]

max_val = 0
for register in registers:
	if max_val < registers[register]:
		max_val = registers[register]

print(max_val_ever_held)
