with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

group_answers = []

curr_group = {}

i = 0
for line in lines:
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
    group = group_answers[i]
    # print(group)
    questions = list(group[list(group.keys())[0]])  # get first person's answers to compare other answers to

    for person in group:
        # print(person, group[person])
        i = 0
        removed_questions_offset = 0
        while i - removed_questions_offset < len(questions):
            question = questions[i - removed_questions_offset]
            # print(i - removed_questions_offset, question, questions)
            if question not in group[person]:
                questions.remove(question)
                # print(f"\tremoved question {question}", questions)
                removed_questions_offset += 1
            i += 1
        # print()

    question_counts.append(len(questions))
    total_count += len(questions)

print(total_count)

