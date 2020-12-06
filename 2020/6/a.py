with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

group_answers = []

curr_group = {}

i = 0
for line in lines:
    print(line)
    if len(line) == 0:
        group_answers.append(curr_group)
        i = 0
        curr_group = {}
        continue

    curr_group[i] = line
    i += 1  # per-group person index

if curr_group:
    group_answers.append(curr_group)

total_count = 0
question_counts = []

for i in range(len(group_answers)):
    questions = []
    group = group_answers[i]
    for person in group:
        print(person, group[person])
        for question in group[person]:
            if question not in questions:
                questions.append(question)
    question_counts.append(len(questions))
    total_count += len(questions)
    print(len(questions))

print(total_count)

