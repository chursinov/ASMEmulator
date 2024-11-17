from command.stack_command import *
from command.arithmetic_command import *
from command.coniditionals_command import *
import vars

def execute_cmd(command):
    match command:
        case 'PUSH_PC_REVSTACK':
            PUSH_PC_REVSTACK(command)
        case 'POP_STACK':
            POP_STACK(command)
        case 'CMP_MEM_STACK':
            CMP_MEM_STACK(command)
        case 'POP_STACK_IF_S':
            POP_STACK_IF_S(command)
        case 'ADD_REVSTACK_4':
            ADD_REVSTACK_4(command)
        case 'JNS_RS':
            JNS_RS(command)
        case 'JNE_RS':
            JNE_RS(command)
        case 'CHECK_STACK_NOT_EMPTY':
            CHECK_STACK_NOT_EMPTY(command)
        case _:
            raise Exception(f"unknown command {command}")