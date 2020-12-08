accumulator = 0
pc = 0

def increment_pc(value=1):
    global pc
    print("\t\t\tinc pc", pc, value)
    pc += value


def acc(value):
    global accumulator
    accumulator += value
    increment_pc()
    return accumulator


def jmp(value):
    increment_pc(value)
    return


def nop(value):
    increment_pc()
    return


operations = {
    "acc": acc,
    "jmp": jmp,
    "nop": nop
}


with open("input", "r") as f:
    lines = f.readlines()
    boot_code = [(instruction[0], int(instruction[1])) for instruction in [line.split() for line in lines]]

visited_instructions = []
while pc < len(boot_code):
    print(pc, boot_code[pc])
    if pc in visited_instructions:
        break
    visited_instructions.append(pc)
    command = boot_code[pc][0]
    argument = boot_code[pc][1]
    operations[command](argument)

print(accumulator)
