from copy import deepcopy


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

end_reached = False

change_location = 0
while not end_reached:
    aux_boot_code = deepcopy(boot_code)
    while True:  # loop to find the next nop or jmp
        if aux_boot_code[change_location][0] in ["nop", "jmp"]:
            original_command = aux_boot_code[change_location][0]
            argument = aux_boot_code[change_location][1]
            new_command = "nop" if original_command == "jmp" else "jmp"
            aux_boot_code[change_location] = (new_command, argument)
            break
        change_location += 1

    pc = 0
    accumulator = 0
    end_reached = True
    visited_instructions = []
    while pc < len(boot_code):
        print(pc, aux_boot_code[pc])
        if pc in visited_instructions:
            end_reached = False
            break
        visited_instructions.append(pc)
        command = aux_boot_code[pc][0]
        argument = aux_boot_code[pc][1]
        operations[command](argument)
    change_location += 1

print(accumulator)
