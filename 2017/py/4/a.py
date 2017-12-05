valid_count = 0

#while True:
with open("in.txt") as f:
	lines = f.read().split('\n')
	for line in lines:
		passphrase = line.split()
		print(passphrase)
		words = []
		invalid = False

		for password in passphrase:
			if password in words:
				invalid = True
				break
			else:
				words.append(password)
				
		if invalid:
			continue
		else:
			valid_count += 1

print(valid_count)