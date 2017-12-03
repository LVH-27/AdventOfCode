spreadsheet = []

with open("in.txt") as f:
	rows = f.read().split('\n')
	for row in rows:
		spreadsheet.append([int(cell) for cell in row.split()])

chksum = 0

for row in spreadsheet:
	chksum += max(row) - min(row)

print(chksum)