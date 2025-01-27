def proc_instr(instr, idx=0, curr=""):
    if idx >= len(instr):  # Base case: end of instructions
        return
    ch = instr[idx]
    if ch.isalpha():
        proc_instr(instr, idx + 1, curr + ch)
    elif ch in "+-":
        val, j = "", idx + 1
        while j < len(instr) and instr[j].isdigit():
            val += instr[j]
            j += 1
        print(f"{curr} {'tighten' if ch == '+' else 'loosen'} {val}")
        proc_instr(instr, j, "")  # Reset curr after action
    else:
        proc_instr(instr, idx + 1, curr)


instr = input()
proc_instr(instr)
