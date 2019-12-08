from aocd import get_data, submit
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
    print(parameter_mode, ops)
    program[result] = ops[0] + ops[1]


def opcode_2(parameter_mode, ops, result):
    ops = get_ops(ops, parameter_mode)

    program[result] = ops[0] * ops[1]


def opcode_3(parameter_mode, ops, test_input):
    # ops = get_ops(ops, parameter_mode)
    program[ops[0]] = test_input


def opcode_4(parameter_mode, ops):
    # ops = get_ops(ops, parameter_mode)
    return program[ops[0]]


def opcode_5(parameter_mode, ops, pos):
    ops = get_ops(ops, parameter_mode)
    return ops[1] if ops[0] != 0 else pos


def opcode_6(parameter_mode, ops, pos):
    ops = get_ops(ops, parameter_mode)
    return ops[1] if ops[0] == 0 else pos


def opcode_7(parameter_mode, ops, pos):
    ops = get_ops(ops, parameter_mode)
    program[ops[2]] = int(ops[0] < ops[1])


def opcode_8(parameter_mode, ops, pos):
    ops = get_ops(ops, parameter_mode)
    program[ops[2]] = int(ops[0] == ops[1])


if exists("input.txt"):
    with open("input.txt") as f:
        data = f.read()
    program = [int(op) for op in data.split(',')]
else:
    data = get_data(day=5, year=2019)
    with open("input.txt", "w") as f:
        f.write(data)
    program = [int(op) for op in data.split(',')]

pos = 0
output_monitor = []
while True:
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
        opcode_3(parameter_mode, ops, test_input=1)
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
        ops = [program[pos + 1], program[pos + 2], program[pos + 3]]
        opcode_7(parameter_mode, ops)
        pos += 4
    elif opcode == 8:
        ops = [program[pos + 1], program[pos + 2], program[pos + 3]]
        opcode_8(parameter_mode, ops)
        pos += 4

print(output_monitor)
result = str(output_monitor[-1])
# submit(result, part='a', day='5', year='2019')
