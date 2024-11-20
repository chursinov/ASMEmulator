import vars

def PUSH_PC_REVSTACK(command):
    vars.reverse_stack_pointer += 1
    vars.common_mem[vars.REVERSE_STACK_BP + vars.reverse_stack_pointer] = vars.pc - 1
    print("cmd = ", command)

def POP_STACK(command):
    vars.common_mem[vars.DATA_BP + vars.data_pointer] = vars.common_mem[vars.STACK_BP + vars.stack_pointer]
    #print(count_len_of_stack(stack))
    #shift_elements_after_pop(vars.stack_pointer, vars.STACK_BP)
    vars.common_mem[vars.STACK_BP + vars.stack_pointer] = ''
    vars.stack_pointer -= 1
    print("cmd = ", command)

def POP_STACK_IF_S(command):
    if vars.SF == 1:
        vars.common_mem[vars.DATA_BP + vars.data_pointer] = vars.common_mem[vars.STACK_BP + vars.stack_pointer]
    #print(count_len_of_stack(stack))
    #shift_elements_after_pop(vars.stack_pointer, vars.STACK_BP)
    vars.common_mem[vars.STACK_BP + vars.stack_pointer] = ''
    vars.stack_pointer -= 1
    print("cmd = ", command)


# def count_len_of_stack(stack):
#     count = 0
#     for element in stack:
#         if element == '':
#             break
#         count += 1
#     return count

# def shift_elements_after_pop(pointer, base_pointer):
#     vars.common_mem[pointer + base_pointer] = ''





