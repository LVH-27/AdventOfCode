class CircularList(list):
	def __getitem__(self, key):
		return list.__getitem__(self, key % len(self))

	def __setitem__(self, key, item):
		list.__setitem__(self, key % len(self), item)


def distribute(block_index, blocks):

	to_distribute = blocks[block_index]
	blocks[block_index] = 0

	for j in range(to_distribute):
		blocks[block_index + j + 1] += 1

	return (max(blocks), blocks)


blocks = CircularList([int(x) for x in input().split()])

max_block_fill = max(blocks)
block_states = [CircularList(blocks)]  # cast to copy

i = 0
while True:
	if blocks[i] == max_block_fill:
		aux_blocks = CircularList(blocks)
		max_block_fill, aux_blocks = distribute(i, aux_blocks)

		block_states.append(aux_blocks)

		if aux_blocks in block_states[:-1]:  # we're done!
			break
		else:
			blocks = aux_blocks
			i = 0
			continue
	i += 1


target_block_state = block_states[-1]
print(block_states[-1])

i = 0
while block_states[i] != target_block_state:
	i += 1  # loop getting the index of loop start

print(len(block_states) - i)


