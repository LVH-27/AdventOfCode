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
				pw_letter_dict = {}
				for letter in password:
					if letter not in pw_letter_dict:
						pw_letter_dict[letter] = 1
					else:
						pw_letter_dict[letter] += 1

				if pw_letter_dict in words:
					invalid = True
					break
				else:
					words.append(pw_letter_dict)
				
		if invalid:
			continue
		else:
			valid_count += 1

print(valid_count)