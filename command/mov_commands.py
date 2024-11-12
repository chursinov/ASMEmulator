import vars
def MOV_RAM_A(command):
    vars.A = vars.common_mem[vars.dp]
    code = 0b1
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_RAM_B(command):
    vars.B = vars.common_mem[vars.dp]
    code = 0b10
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_RAM_C(command):
    vars.C = vars.common_mem[vars.dp]
    code = 0b11
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_PC_MARK_A(command):
    vars.MARK_A = vars.pc
    code = 0b100
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_PC_MARK_B(command):
    vars.MARK_B = vars.pc
    code = 0b101
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_PC_MARK_C(command):
    vars.MARK_C = vars.pc
    code = 0b110
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_B_A(command):
    vars.A = vars.B
    code = 0b111
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_B_C(command):
    vars.C = vars.B
    code = 0b1000
    print("cmd = ", command, "binary = ", bin(code)[2:])

def  MOV_A_B(command):
    vars.B = vars.A
    code = 0b1001
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_A_C(command):
    vars.C = vars.A
    code = 0b1010
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_C_A(command):
    vars.A = vars.C
    code = 0b1011
    print("cmd = ", command, "binary = ", bin(code)[2:])

def MOV_C_B(command):
    vars.B = vars.C
    code = 0b1100
    print("cmd = ", command, "binary = ", bin(code)[2:])