import vars
#JS
def JS_MARK_B(command):
    if vars.SF == 1:
        vars.pc = vars.MARK_B
        vars.SF = 0
    code = 0b1110
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JS_MARK_A(command):
    if vars.SF == 1:
        vars.pc = vars.MARK_A
        vars.SF = 0
    code = 0b1101
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JS_MARK_C(command):
    if vars.SF == 1:
        vars.pc = vars.MARK_C
        vars.SF = 0
    code = 0b11011
    print("cmd = ", command, "binary = ", bin(code)[2:])

#JNS
def JNS_MARK_A(command):
    if vars.SF == 0:
        vars.pc = vars.MARK_A
    code = 0b1111
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JNS_MARK_B(command):
    if vars.SF == 0:
        vars.pc = vars.MARK_B
    code = 0b10000
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JNS_MARK_C(command):
    if vars.SF == 0:
        vars.pc = vars.MARK_C
    code = 0b10001
    print("cmd = ", command, "binary = ", bin(code)[2:])


#JNZ
def JNZ_MARK_C(command):
    if vars.ZF == 0:
        vars.pc = vars.MARK_C
    code = 0b10010
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JNZ_MARK_B(command):
    if vars.ZF == 0:
        vars.pc = vars.MARK_B
    code = 0b10011
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JNZ_MARK_A(command):
    if vars.ZF == 0:
        vars.pc = vars.MARK_A
    code = 0b10100
    print("cmd = ", command, "binary = ", bin(code)[2:])

#JZ
def JS_MARK_B(command):
    if vars.ZF == 1:
        vars.pc = vars.MARK_B
        vars.ZF = 0
    code = 0b10101
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JS_MARK_A(command):
    if vars.ZF == 1:
        vars.pc = vars.MARK_A
        vars.ZF = 0
    code = 0b10110
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JS_MARK_C(command):
    if vars.ZF == 1:
        vars.pc = vars.MARK_C
        vars.ZF = 0
    code = 0b10111
    print("cmd = ", command, "binary = ", bin(code)[2:])

#JMP
def JMP_MARK_A(command):
    vars.pc = vars.MARK_A
    code = 0b11000
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JMP_MARK_B(command):
    vars.pc = vars.MARK_B
    code = 0b11001
    print("cmd = ", command, "binary = ", bin(code)[2:])

def JMP_MARK_C(command):
    vars.pc = vars.MARK_C
    code = 0b11010
    print("cmd = ", command, "binary = ", bin(code)[2:])