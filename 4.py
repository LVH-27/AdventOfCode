A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

class InputLine:

	def __init__(self, line):
		self.stats = {1: []}
		self.line = line
		aux = self.line.split('-')
		self.letters = aux[:-1]
		self.sid, self.checksum = aux[-1].split('[')
		self.checksum = self.checksum[:-1]
		self.realChecksum = calculateChecksum()

		auxs = ''
		for s in self.letters:
			auxs += s
		self.letters = str(auxs)
		getLetterStats()

		def getLetterStats():
			appearedLetters = []
			maxkey = 1
			for c in self.letters:
				if c not in appearedLetters:
					appearedLetters.append(c)
					self.stats[1].append(c)
				else:
					for i in range(1, maxkey):
						if c in self.stats[i]:
							self.stats[i].remove(c)
							if i+1 not in self.stats:
								self.stats[i+1] = [c]
								maxkey = i+1
							else:
								self.stats[i+1].append(c)
							break

			for stat in stats:
				stat = sorted(stat)

	def calculateChecksum(self):
		
