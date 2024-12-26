import vars

def JZ(command):
    if vars.ZF == 1:
        vars.pc = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1] - 1
        vars.ZF = 0
    vars.stack_pointer -= 1

def JNZ(command):
    if vars.ZF == 0:
        vars.pc = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1] - 1
    vars.stack_pointer -= 1

def JNS(command):
    if vars.SF == 0:
        vars.pc = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1] - 1
    vars.stack_pointer -= 1

def JS(command):
    if vars.SF == 1:
        vars.pc = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1] - 1
        vars.SF = 0
    vars.stack_pointer -= 1

def JMP(command):
    vars.pc = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1] - 1
    vars.stack_pointer -= 1