total = 0
in_string = input()

for i in range(len(in_string)):
	print("Last: ", in_string[i])
	curr_digit = in_string[i]
	next_digit = in_string[0] if i == len(in_string) - 1 else in_string[i + 1]
	if curr_digit == next_digit:
		total += int(curr_digit)

print(total)
