import vars

# def JNS_RS(command):
#     if vars.SF != 1:
#         vars.pc = vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer]
#     vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer] = ''
#     vars.reverse_stack_pointer -= 1
#     print("cmd = ", command)

# def JNE_RS(command):
#     if vars.EF != 1:
#         vars.pc = vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer]
#     vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer] = ''
#     vars.reverse_stack_pointer -= 1
#     print("cmd = ", command)

# def JS_RS(command):
#     if vars.SF == 1:
#         vars.pc = vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer]
#     vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer] = ''
#     vars.reverse_stack_pointer -= 1
#     print("cmd = ", command)

# def JE_RS(command):
#     if vars.SF == 1:
#         vars.pc = vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer]
#     vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer] = ''
#     vars.reverse_stack_pointer -= 1
#     print("cmd = ", command)


# def CHECK_STACK_NOT_EMPTY(command):
#     if vars.stack_pointer == -1:
#         vars.EF = 1
#     print("cmd = ", command)

def JZ_20(command):
    if vars.ZF == 1:
        vars.pc = 20 - 1
        vars.ZF = 0

def JNZ_11(command):
    if vars.ZF == 0:
        vars.pc = 11 - 1

def JNS_11(command):
    if vars.SF == 0:
        vars.pc = 11 - 1

def JS_20(command):
    if vars.SF == 1:
        vars.pc = 20 - 1
        vars.SF = 0