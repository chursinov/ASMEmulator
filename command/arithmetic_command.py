import vars

def CMP(command):
    result = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 2] - vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1]
    if result < 0:
        vars.SF = 1
    elif result == 0:
        vars.ZF = 1
    else:
        vars.SF = 0
        vars.ZF = 0

def INC_ST(command):
    vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1] += 1

def DCR_ST(command):
    vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1] -= 1