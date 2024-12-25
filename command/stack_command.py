import vars

def PUSH_256(command):
    vars.common_mem[vars.STACK_BP + vars.stack_pointer] = 256
    vars.stack_pointer += 1

def DUP(command):
    vars.common_mem[vars.STACK_BP + vars.stack_pointer] = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1]
    vars.stack_pointer += 1

def READ_MEM(command):
    addr = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1]
    vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1] = vars.common_mem[int(addr)]

def SWAP(command):
    vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1],vars.common_mem[vars.STACK_BP + vars.stack_pointer - 2] = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 2],vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1]

def DROP(command):
    vars.common_mem[vars.STACK_BP + vars.stack_pointer] = ''
    vars.stack_pointer -= 1

def ROT(command):
    buf = vars.common_mem[vars.STACK_BP + vars.stack_pointer - 1]
    for i in range(vars.STACK_BP + vars.stack_pointer - 2, vars.STACK_BP - 1, -1):
        vars.common_mem[i + 1] = vars.common_mem[i]
    vars.common_mem[vars.STACK_BP] = buf