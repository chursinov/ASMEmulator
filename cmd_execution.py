from command.stack_command import *
from command.arithmetic_command import *
from command.coniditionals_command import *
import vars

def execute_cmd(command):
    match command:
        case 'PUSH_256':
            PUSH_256(command)
        case 'DUP':
            DUP(command)
        case 'READ_MEM':
            READ_MEM(command)
        case 'CMP_1':
            CMP_1(command)
        case 'SWAP':
            SWAP(command)
        case 'DROP':
            DROP(command)
        case 'INC_ST':
            INC_ST(command)
        case 'ROT':
            ROT(command)
        case 'CMP':
            CMP(command)
        case 'JZ_20':
            JZ_20(command)
        case 'JNZ_11':
            JNZ_11(command)
        case 'JS_20':
            JS_20(command)
        case 'JNS_11':
            JNS_11(command)
        case _:
            raise Exception(f"unknown command {command}")