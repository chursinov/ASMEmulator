from cmd_execution import execute_cmd
import vars

replacements_dict = {
    'PUSH': 0b0001,
    'READ_MEM': 0b0010,
    'SWAP': 0b0011,
    'DUP': 0b0100,
    'DROP':0b0110,
    'ROT': 0b0101,
    'CMP': 0b0111,
    'INC_ST': 0b1000,
    'DCR_ST':0b1001,
    'JNS': 0b1010,
    'JNZ': 0b1011,
    'JZ': 0b1100,
    'JS':0b1101,
    'JMP':0b1110,
    'END': 0b0000
}

def main():
    with open("input.txt", "r") as file:
        i = 0
        while True:
            line = file.readline()
            if line == "":
                break
            vars.common_mem[i] = line.strip()
            i += 1
    #print(f"com = {vars.common_mem[0:30]}")
    vars.common_mem = [replacements_dict.get(x, x) for x in vars.common_mem]
    while(1):
        cmd = vars.common_mem[vars.pc]
        print("pc = ", bin(vars.pc), "cmd = ", bin(cmd),"stack =", list(map(bin, vars.common_mem[512:512 + vars.stack_pointer])))
        if vars.common_mem[vars.pc] == 0b0000:
            break
        execute_cmd(cmd)
        vars.pc += 1
    print()
    print("_____Конец Вычислений_______")
    print("PC = ", bin(vars.pc))
    print("stack =", list(map(bin,vars.common_mem[512:512 + vars.stack_pointer])))
    print("stack pointer = ", bin(vars.stack_pointer))
    print("ZF = ", bin(vars.ZF))
    print("SF = ", bin(vars.SF))



if __name__ == "__main__":
    main()