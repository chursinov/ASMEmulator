from cmd_execution import execute_cmd
import command.mov_commands as mov_commands
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
            print("cmd = ", "END", "binary = ", "111111")
            break
        execute_cmd(cmd)
        vars.pc += 1
    print()
    print("_____Конец Вычислений_______")
    print("A = ", vars.A)
    print("B = ", vars.B)
    print("C = ", vars.C)
    print("DP = ", vars.dp)
    print("PC = ", vars.pc)
    print("MARK_A = ", vars.MARK_A)
    print("MARK B = ", vars.MARK_B)
    print("MARK C = ", vars.MARK_C)
    print("ZF = ", vars.ZF)
    print("SF = ", vars.SF)


if __name__ == "__main__":
    main()