from command.stack_command import *
from command.arithmetic_command import *
from command.coniditionals_command import *
import vars

def execute_cmd(command):
    match command:
        case 'PUSH':
            PUSH(command)
        case 'DUP':
            DUP(command)
        case 'READ_MEM':
            READ_MEM(command)
        case 'CMP':
            CMP(command)
        case 'SWAP':
            SWAP(command)
        case 'DROP':
            DROP(command)
        case 'INC_ST':
            INC_ST(command)
        case 'DCR_ST':
            DCR_ST(command)
        case 'ROT':
            ROT(command)
        case 'JZ':
            JZ(command)
        case 'JNZ':
            JNZ(command)
        case 'JS':
            JS(command)
        case 'JNS':
            JNS(command)
        case _:
            raise Exception(f"unknown command {command}")