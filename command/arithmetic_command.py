import vars


def INC_DP(command):
    vars.dp += 1
    code = 0b11100
    print("cmd = ", command, "binary = ", bin(code)[2:])

def DCR_C(command):
    vars.C -= 1
    code = 0b11101
    print("cmd = ", command, "binary = ", bin(code)[2:])

def ADD_MARK_A_1(command):
    vars.MARK_A += 1
    code = 0b11110
    print("cmd = ", command, "binary = ", bin(code)[2:])

def ADD_MARK_B_1(command):
    vars.MARK_B += 1
    code = 0b11111
    print("cmd = ", command, "binary = ", bin(code)[2:])

def ADD_MARK_C_1(command):
    vars.MARK_C += 1
    code = 0b100000
    print("cmd = ", command, "binary = ", bin(code)[2:])

def CMP_C_1(command):
    result = vars.C - 1
    if result == 0:
        vars.ZF = 1
    code = 0b100001
    print("cmd = ", command, "binary = ", bin(code)[2:])

def CMP_A_B(command):
    result = vars.A - vars.B
    if result < 0:
        vars.SF = 1
    elif result == 0:
        vars.ZF = 2
    code = 0b100010
    print("cmd = ", command, "binary = ", bin(code)[2:])

def ADD_MARK_B_5(command):
    vars.MARK_B += 5
    code = 0b100011
    print("cmd = ", command, "binary = ", bin(code)[2:])

def ADD_MARK_C_4(command):
    vars.MARK_C += 4
    code = 0b100100
    print("cmd = ", command, "binary = ", bin(code)[2:])