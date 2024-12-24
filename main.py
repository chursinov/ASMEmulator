from cmd_execution import execute_cmd
import vars

def main():
    with open("input.txt", "r") as file:
        i = 0
        while True:
            line = file.readline()
            if line == "":
                break
            vars.common_mem[i] = line.strip()
            i += 1
    print(f"com = {vars.common_mem[0:30]}")
    while(1):
        cmd = vars.common_mem[vars.pc]
        print("pc = ", vars.pc, "cmd = ", cmd)
        if vars.common_mem[vars.pc] == 'END':
            break
        execute_cmd(cmd)
        vars.pc += 1
    print()
    print("_____Конец Вычислений_______")
    print("PC = ", vars.pc)
    print("stack =", vars.common_mem[512:512 + vars.stack_pointer])
    print("stack pointer = ", vars.stack_pointer)
    print("ZF = ", vars.ZF)
    #print("command = ", vars.common_mem[0:10])



if __name__ == "__main__":
    main()