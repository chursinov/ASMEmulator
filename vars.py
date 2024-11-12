pc = 0
common_mem = [0] * 1024
cmd = ""
CMD_SIZE = 512
dp = CMD_SIZE

A = 0
B = 0
C = 0

MARK_A = 0
MARK_B = 0
MARK_C = 0

ZF = 0
SF = 0


# common_mem[0] = "MOV_RAM_C"
# common_mem[1] = "INC_DP"
# common_mem[2] = "MOV_RAM_A"
# common_mem[3] = "INC_DP"
# common_mem[4] = "MOV_PC_MARK_A"
# common_mem[5] = "ADD_MARK_A_1"
# common_mem[6] = "CMP_C_1"
# common_mem[7] = "DCR_C"
# common_mem[8] = "MOV_RAM_B"
# common_mem[9] = "INC_DP"
# common_mem[10] = "CMP_A_B"
# common_mem[11] = "MOV_PC_MARK_B"
# common_mem[12] = "ADD_MARK_B_5"
# common_mem[13] = "MOV_PC_MARK_C"
# common_mem[14] = "ADD_MARK_C_4"
# common_mem[15] = "JS_MARK_B"
# common_mem[16] = "JMP_MARK_C"
# common_mem[17] = "MOV_B_A"
# common_mem[18] = "JNZ_MARK_A"
# common_mem[19] = "END"

common_mem[512] = 4
common_mem[513] = 155
common_mem[514] = 22
common_mem[515] = 206
common_mem[132] = 45