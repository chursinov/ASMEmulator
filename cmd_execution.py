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
        case 0b1:
            PUSH_256(command)
        case 0b10:
            READ_MEM(command)
        case 0b11:
            SWAP(command)
        case 0b100:
            DUP(command)
        case 0b101:
            ROT(command)
        case 0b111:
            CMP(command)
        case 0b1000:
            CMP_1(command)
        case 0b1001:
            INC_ST(command)
        case 0b1101:
            JS_20(command)
        case 0b1011:
            JNZ_11(command)
        case 0b0110:
            DROP(command)
        case _:
            raise Exception(f"unknown command {command}")