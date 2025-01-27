instructions, current_string, i = input(), "", 0
while i < len(instructions):
    char = instructions[i]
    if char.isalpha():
        current_string += char
    elif char in "+-":
        i += 1
        value = ""
        while i < len(instructions) and instructions[i].isdigit():
            value += instructions[i]
            i += 1
        print(f"{current_string} {'tighten' if char == '+' else 'loosen'} {value}")
        current_string = ""
        continue
    i += 1
