import sys

if sys.argv[1].lower() not in ['first', 'second']:
    sys.exit(-1)

def execute(prog, ptr, acc):
    if (ptr < 0) or (ptr >= len(prog)):
        return len(prog), acc
    op, arg = prog[ptr]
    if op == "nop":
        return ptr+1, acc
    if op == "acc":
        return ptr+1, acc+arg
    if op == "jmp":
        return ptr+arg, acc
    raise NotImplementedError(f"Op code '{op}' is not yet implemented")

with open('../input.txt') as FILE:
    code = [l.strip().split() for l in FILE.readlines()]
    code = [(c[0], int(c[1])) for c in code]

ACC = 0
PTR = 0
executed = set()
while PTR not in executed:
    executed.add(PTR)
    PTR, ACC = execute(code, PTR, ACC)
    
if sys.argv[1].lower() == 'first':
    print("Final pointer:    ", PTR)
    print("Final accumulator:", ACC)
    sys.exit(0)

TERM = len(code)

candidates = [e for e in executed if code[e][0] in ['nop', 'jmp']]

for cand in candidates:
    new_code = code[:]
    if new_code[cand][0] == 'jmp':
        new_code[cand] = ('nop', new_code[cand][1])
    elif new_code[cand][0] == 'nop':
        new_code[cand] = ('jmp', new_code[cand][1])
    else:
        raise ValueError("Candidate instruction should be 'nop' or 'jmp'")
    new_acc = 0
    new_ptr = 0
    new_exec = set()
    while new_ptr not in new_exec:
        new_exec.add(new_ptr)
        new_ptr, new_acc = execute(new_code, new_ptr, new_acc)
    if new_ptr == TERM:
        print("Altered operation:", cand)
        print("Final pointer:    ", new_ptr)
        print("Final accumulator:", new_acc)
        break
