spreadsheet = []

with open("in.txt") as f:
	rows = f.read().split('\n')
	for row in rows:
		spreadsheet.append([int(cell) for cell in row.split()])

chksum = 0

for row in spreadsheet:
	found = False
	for i in range(len(row)):

		if found:  # if an even division was found, break and go to the next row
				break

		for j in range(len(row)):
			if j == i:  # one can always divide itself by itself
				continue
			if found:  # if an even division was found, break and go to the next row
				break

			if row[i] % row[j] == 0 or row[j] % row[i] == 0:
				found = True
				numerator = max(row[i], row[j])
				denominator = min(row[i], row[j])
				chksum += numerator / denominator


print(chksum)
