from aocd import get_data, submit
from itertools import permutations
from os.path import exists


def get_ops(ops, parameter_mode):
    if len(parameter_mode) < len(ops):
        parameter_mode.extend([0 for i in range(len(ops) - len(parameter_mode))])

    for i in range(len(parameter_mode)):
        parameter = int(parameter_mode[i])
        ops[i] = program[ops[i]] if parameter == 0 else ops[i]
    return ops


def opcode_1(parameter_mode, ops, result):
    ops = get_ops(ops, parameter_mode)
    program[result] = ops[0] + ops[1]


def opcode_2(parameter_mode, ops, result):
    ops = get_ops(ops, parameter_mode)

    program[result] = ops[0] * ops[1]


def opcode_3(parameter_mode, ops, test_input):
    # ops = get_ops(ops, parameter_mode)
    print()
    print(f"Test input: {test_input}")
    print(f"Ops: {ops}")
    print()
    program[ops[0]] = test_input


def opcode_4(parameter_mode, ops):
    ops = get_ops(ops, parameter_mode)
    print()
    print("TU: ", ops)
    print()
    return ops[0]


def opcode_5(parameter_mode, ops, pos):
    ops = get_ops(ops, parameter_mode)
    return ops[1] if ops[0] != 0 else pos + 3


def opcode_6(parameter_mode, ops, pos):
    ops = get_ops(ops, parameter_mode)
    return ops[1] if ops[0] == 0 else pos + 3


def opcode_7(parameter_mode, ops, result):
    ops = get_ops(ops, parameter_mode)
    program[result] = int(ops[0] < ops[1])


def opcode_8(parameter_mode, ops, result):
    ops = get_ops(ops, parameter_mode)
    program[result] = int(ops[0] == ops[1])


if exists("input.txt"):
    with open("input.txt") as f:
        data = f.read()
    initial_program = [int(op) for op in data.split(',')]
else:
    data = get_data(day=7, year=2019)
    with open("input.txt", "w") as f:
        f.write(data)
    initial_program = [int(op) for op in data.split(',')]

pos = 0
phase_setting_permutations = permutations(range(0, 5))
max_signal = 0

for perm in phase_setting_permutations:
    print(f"Perm: {perm}")
    output_monitor = []
    program = initial_program
    prev_output = 0
    for i in range(len(perm)):
        pos = 0
        phase_setting = perm[i]
        inputs = [prev_output, phase_setting]  # reverse order of inputs because of popping
        while True:
            print(f"Program prije poziva: {program}")
            print(f"Pos: {pos}, instruction: {program[pos]}; inputs: {inputs}")
            # input()
            instruction = str(program[pos])
            parameter_mode = list(instruction[:-2][::-1])
            opcode = int(instruction[-2:])
            if opcode == 99:
                break

            if opcode == 1:
                ops = [program[pos + 1], program[pos + 2]]
                result = program[pos + 3]
                opcode_1(parameter_mode, ops, result)
                pos += 4
            elif opcode == 2:
                ops = [program[pos + 1], program[pos + 2]]
                result = program[pos + 3]
                opcode_2(parameter_mode, ops, result)
                pos += 4
            elif opcode == 3:
                ops = [program[pos + 1]]
                opcode_3(parameter_mode, ops, test_input=inputs.pop())
                pos += 2
            elif opcode == 4:
                ops = [program[pos + 1]]
                output_monitor.append(opcode_4(parameter_mode, ops))
                pos += 2
            elif opcode == 5:
                ops = [program[pos + 1], program[pos + 2]]
                pos = opcode_5(parameter_mode, ops, pos)
            elif opcode == 6:
                ops = [program[pos + 1], program[pos + 2]]
                pos = opcode_6(parameter_mode, ops, pos)
            elif opcode == 7:
                ops = [program[pos + 1], program[pos + 2]]
                result = program[pos + 3]
                opcode_7(parameter_mode, ops, result)
                pos += 4
            elif opcode == 8:
                ops = [program[pos + 1], program[pos + 2]]
                result = program[pos + 3]
                opcode_8(parameter_mode, ops, result)
                pos += 4
        prev_output = output_monitor[-1]
    print(f"Perm: {perm}, output_monitor: {output_monitor}")
    if prev_output > max_signal:
        max_signal = prev_output

print(max_signal)
result = max_signal

# submit(result, part='a', day=7, year=2019)
