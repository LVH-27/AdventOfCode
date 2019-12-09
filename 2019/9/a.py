# from aocd import get_data, submit
from collections import defaultdict
from os.path import exists
import sys
from copy import deepcopy


class DefaultDict(defaultdict):
    def __missing__(self, key):
        return 0


def get_ops(ops, parameter_mode):
    if len(parameter_mode) < len(ops):
        parameter_mode.extend([0 for i in range(len(ops) - len(parameter_mode))])

    for i in range(len(parameter_mode)):
        parameter = int(parameter_mode[i])
        if parameter == 0:
            ops[i] = program[ops[i]]
        elif parameter == 1:
            ops[i] = ops[i]
        elif parameter == 2:
            ops[i] = program[ops[i] + relative_base]
    return ops


def get_result_address(result, parameter_mode):
    if parameter_mode == 0:
        return result
    elif parameter_mode == 2:
        return result + relative_base


def opcode_1(parameter_mode, ops, result):
    if len(parameter_mode) > len(ops):
        result_parameter_mode = parameter_mode.pop()
        result = get_result_address(result, result_parameter_mode)
    ops = get_ops(ops, parameter_mode)
    program[result] = ops[0] + ops[1]


def opcode_2(parameter_mode, ops, result):
    if len(parameter_mode) > len(ops):
        result_parameter_mode = parameter_mode.pop()
        result = get_result_address(result, result_parameter_mode)
    ops = get_ops(ops, parameter_mode)

    program[result] = ops[0] * ops[1]


def opcode_3(parameter_mode, ops, test_input):
    # ops = get_ops(ops, parameter_mode)
    ops[0] = ops[0] + relative_base
    program[ops[0]] = test_input


def opcode_4(parameter_mode, ops):
    ops = get_ops(ops, parameter_mode)
    return ops[0]


def opcode_5(parameter_mode, ops, pos):
    ops = get_ops(ops, parameter_mode)
    return ops[1] if ops[0] != 0 else pos + 3


def opcode_6(parameter_mode, ops, pos):
    ops = get_ops(ops, parameter_mode)
    return ops[1] if ops[0] == 0 else pos + 3


def opcode_7(parameter_mode, ops, result):
    if len(parameter_mode) > len(ops):
        result_parameter_mode = parameter_mode.pop()
        result = get_result_address(result, result_parameter_mode)
    ops = get_ops(ops, parameter_mode)
    program[result] = int(ops[0] < ops[1])


def opcode_8(parameter_mode, ops, result):
    if len(parameter_mode) > len(ops):
        result_parameter_mode = parameter_mode.pop()
        result = get_result_address(result, result_parameter_mode)
    print(ops, result, parameter_mode)
    ops = get_ops(ops, parameter_mode)
    program[result] = int(ops[0] == ops[1])


def opcode_9(parameter_mode, ops):
    ops = get_ops(ops, parameter_mode)
    return relative_base + ops[0]


# if exists("input.txt"):
#     with open("input.txt") as f:
#         data = f.read()
#     data = [int(op) for op in data.split(',')]
# else:
#     data = get_data(day=7, year=2019)
#     with open("input.txt", "w") as f:
#         f.write(data)
#     data = [int(op) for op in data.split(',')]

with open(sys.argv[1]) as f:
    data = f.read()
data = [int(op) for op in data.split(',')]

pos = 0
relative_base = 0
output_monitor = []
initial_program = DefaultDict()
for i in range(len(data)):
    initial_program[i] = data[i]
program = deepcopy(initial_program)
input_value = 1

while True:
    # print(f"Program prije poziva: {program}")
    print(f"Pos: {pos}, instruction: {program[pos]}; relative_base: {relative_base}")
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
        opcode_3(parameter_mode, ops, test_input=input_value)
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
    elif opcode == 9:
        ops = [program[pos + 1]]
        relative_base = opcode_9(parameter_mode, ops)
        pos += 2


print(output_monitor)
# result = TODO
# print(result)

# submit(result, part='a', day=7, year=2019)
