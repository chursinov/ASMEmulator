import vars

def CMP_MEM_STACK(command):
    vars.SF = 0
    result = vars.common_mem[vars.DATA_BP + vars.data_pointer] - vars.common_mem[vars.STACK_BP + vars.stack_pointer]
    if result < 0:
        vars.SF = 1
    print("cmd = ", command)

def ADD_REVSTACK_4(command):
    vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer] += 4
    print("cmd = ", command)