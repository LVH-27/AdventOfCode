import hashlib
pw = ""

room = str(input())

i = 0
while True:
	m = hashlib.md5((room + str(i)).encode('utf-8'))
	haash = m.hexdigest()

	if haash[:5] == "00000":
		pw += haash[5]
		if len(pw) == 8:
			break
	i += 1

print(pw)
