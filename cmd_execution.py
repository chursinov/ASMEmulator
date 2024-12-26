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
        case 'JMP':
            JMP(command)
        case 0b0001:
            PUSH(command)
        case 0b0010:
            READ_MEM(command)
        case 0b0011:
            SWAP(command)
        case 0b0100:
            DUP(command)
        case 0b0101:
            ROT(command)
        case 0b0110:
            DROP(command)
        case 0b0111:
            CMP(command)
        case 0b1000:
            INC_ST(command)
        case 0b1001:
            DCR_ST(command)
        case 0b1010:
            JNS(command)
        case 0b1011:
            JNZ(command)
        case 0b1100:
            JZ(command)
        case 0b1101:
            JS(command)
        case 0b1110:
            JMP(command)
        case _:
            raise Exception(f"unknown command {command}")