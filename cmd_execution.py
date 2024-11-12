from command.mov_commands import *
from command.arithmetic_command import INC_DP, ADD_MARK_A_1, ADD_MARK_B_5, CMP_C_1, DCR_C, CMP_A_B, ADD_MARK_C_4
from command.conditionals_command import JS_MARK_B, JMP_MARK_A, JMP_MARK_C, JNZ_MARK_C, JNZ_MARK_A

def execute_cmd(command):
    match command:
        case "MOV_RAM_A":
            MOV_RAM_A(command)
        case "MOV_RAM_B":
            MOV_RAM_B(command)
        case "MOV_RAM_C":
            MOV_RAM_C(command)
        case "MOV_PC_MARK_A":
            MOV_PC_MARK_A(command)
        case "ADD_MARK_A_1":
            ADD_MARK_A_1(command)
        case "ADD_MARK_B_5":
            ADD_MARK_B_5(command)
        case "ADD_MARK_C_4":
            ADD_MARK_C_4(command)
        case "INC_DP":
            INC_DP(command)
        case "DCR_C":
            DCR_C(command)
        case "CMP_C_1":
            CMP_C_1(command)
        case "CMP_A_B":
            CMP_A_B(command)
        case "MOV_PC_MARK_B":
            MOV_PC_MARK_B(command)
        case "MOV_PC_MARK_C":
            MOV_PC_MARK_C(command)
        case "MOV_B_A":
            MOV_B_A(command)
        case "JS_MARK_B":
            JS_MARK_B(command)
        case "JMP_MARK_A":
            JMP_MARK_A(command)
        case "JMP_MARK_C":
            JMP_MARK_C(command)
        case "JNZ_MARK_C":
            JNZ_MARK_C(command)
        case "JNZ_MARK_A":
            JNZ_MARK_A(command)
        case _:
            raise Exception(f"unknown command {command}")