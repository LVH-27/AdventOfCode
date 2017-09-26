# A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

#     aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
#     a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
#     not-a-real-room-404[oarel] is a real room.
#     totally-real-room-200[decoy] is not.

# Of the real rooms from the list above, the sum of their sector IDs is 1514.

class InputLine:

	def __init__(self, line):
		self.maxkey = 1
		self.stats = {1: []}
		self.line = line
		aux = self.line.split('-')
		self.letters = aux[:-1]
		self.sid = int(aux[-1].split('[')[0])
		self.checksum = aux[-1].split('[')[1][:-1]
		#self.checksum = self.checksum[:-1]

		auxs = ''
		for s in self.letters:
			auxs += s
		self.letters = str(auxs)
		self.getLetterStats()
		self.realChecksum = self.calculateChecksum()

	def getLetterStats(self):
		appearedLetters = []
		#print(self.stats)
		for c in self.letters:
			if c not in appearedLetters:
				appearedLetters.append(c)
				self.stats[1].append(c)
			else:
				for i in range(1, self.maxkey+1):
					if c in self.stats[i]:
						self.stats[i].remove(c)
						if i+1 not in self.stats:
							self.stats[i+1] = [c]
							self.maxkey = i+1
						else:
							self.stats[i+1].append(c)
						break

		for stat in self.stats:
			#print(self.stats[stat])
			self.stats[stat] = sorted(self.stats[stat])

	def calculateChecksum(self):
		#print(" TEST TEST ")
		#print(self.stats)
		aux = ''
		for i in range(1, self.maxkey+1)[::-1]:
			for c in self.stats[i]:
				aux += c
				if len(aux) == 5:
					break
			if len(aux) == 5:
				break

		return aux

passcode = 0
try:
	while True:
		inputLine = InputLine(input())
		if inputLine.realChecksum == inputLine.checksum:
			passcode += inputLine.sid
except EOFError as e:
	pass
print(passcode)
