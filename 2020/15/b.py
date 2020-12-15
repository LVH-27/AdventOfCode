from collections import defaultdict
import signal
import os


def handler(signum, frame):
    global counter
    print(counter)


signal.signal(signal.SIGUSR1, handler)
print(os.getpid())

with open("input", 'r') as f:
    starting_numbers = [int(n.strip()) for n in f.read().split(',')]

counter = 0
number_timestamps = defaultdict(list)
last_number = 0

while counter < len(starting_numbers):
    number = starting_numbers[counter]
    print(counter, number)
    number_timestamps[number].append(counter)
    last_number = number
    counter += 1

age = 0
while counter < 30000000:
    if len(number_timestamps[last_number]) == 1:  # if it's the first time the last number was spoken
        number = 0  # say zero
    else:
        number = number_timestamps[last_number][-1] - number_timestamps[last_number][-2]  # say the age
    number_timestamps[number].append(counter)
    # print(counter, number, number_timestamps)
    last_number = number
    counter += 1

print(last_number)
