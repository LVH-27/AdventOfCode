import hashlib
pw = ['x' for x in range(8)]
cnt = 0

room = str(input())

i = 0
while True:
	m = hashlib.md5((room + str(i)).encode('utf-8'))
	haash = m.hexdigest()

	if haash[:5] == "00000":
		print(i, haash, pw)
		index = haash[5]
		if index in range(8):
			if pw[index] != 'x':
				pw[index] = haash[6]
				cnt += 1
		if cnt == 8:
			break
	i += 1

print(pw)
