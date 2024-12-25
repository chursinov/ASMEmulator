import vars

def PUSH(command):
    vars.common_mem[vars.STACK_BP + vars.stack_pointer] = int(vars.common_mem[vars.pc + 1])
    vars.stack_pointer += 1
    vars.pc += 1

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