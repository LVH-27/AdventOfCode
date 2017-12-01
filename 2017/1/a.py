class CircularList(list):
	def __getitem__(self, key):
		return list.__getitem__(self, key % len(self))

	def __setitem__(self, key, item):
		list.__setitem__(self, key % len(self), item)


total = 0
in_string = CircularList(input())
step = int(len(in_string) / 2)

for i in range(len(in_string)):
	curr_digit = in_string[i]
	next_digit = in_string[i + step]
	if curr_digit == next_digit:
		total += int(curr_digit)

print(total)
