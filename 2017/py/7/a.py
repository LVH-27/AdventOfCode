programs = {}
def input_programs(filename):
	global programs

	with open(filename) as f:
		lines = f.readlines()


	for line in lines:
		line = line.split(' -> ')
		program_id, program_weight = line[0].split()

		try:
			program_children = [x.strip() for x in line[1].split(", ")]
		except IndexError as e:
			program_children = None

		programs[program_id] = {'weight': program_weight, 
								'children': program_children,
								'parent': None
								}
	
	for program in programs:
		try:
			for child in programs[program]['children']:
				programs[child]['parent'] = program  # set parents to children
		except TypeError as e:
			pass


def get_root_program():
	for program in programs:
		if programs[program]['parent'] is None:
			return program


input_programs("in.txt")
print(get_root_program())

