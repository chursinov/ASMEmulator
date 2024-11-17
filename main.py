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
    print(vars.common_mem[:21])
    while(1):
        cmd = vars.common_mem[vars.pc]
        if vars.common_mem[vars.pc] == "END":
            print("cmd = ", "END")
            break
        execute_cmd(cmd)
        vars.pc += 1
    print()
    print("_____Конец Вычислений_______")
    print("DP = ", vars.data_pointer)
    print("PC = ", vars.pc)
    print("SF = ", vars.SF)
    print("EF = ", vars.EF)
    print("stack =", vars.common_mem[512:520])
    print("reverse stack = ", vars.common_mem[768:780])
    print("reverse_stack_pointer = ", vars.reverse_stack_pointer)
    print("com = ", vars.common_mem[0:10])
    print("data = ", vars.common_mem[vars.DATA_BP:vars.DATA_BP + 10])
    print("len =", len(vars.common_mem))



if __name__ == "__main__":
    main()