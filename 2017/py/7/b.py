class Node:
	def __init__(id, weight, children=None, parent=None):
		self.id = id
		self.weight = weight
		self.children = children
		self.parent = parent
		self.subtree_weight = None

	def calculate_subtree_weight(self):
		if self.subtree_weight is None:
			self.subtree_weight = weight
			try:
				for child in children:
					self.subtree_weight += child.calculate_subtree_weight()
			except TypeError as e:
				pass
			return self.subtree_weight

	def calculate_node_depth(self, root):
		if self == root:
			return 0

		try:
			for child in self.children:
				pass
		except TypeError as e:
			pass


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
								'parent': None,
								'subtree_weight': None
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



def get_unbalanced_node():
	for level


input_programs("in.txt")
print(get_root_program())
print(get_unbalanced_node())
