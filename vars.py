#Счётчик комманд
pc = 0

# Общая память
common_mem = [""] * 1024
cmd = ""

#память данных
DATA_BP = 256

#стэк - храним данные
#стэк - область данных начиная с [512]
STACK_BP = 512
stack_pointer = 0

ZF = 0

#Предзагружаем данные в память
common_mem[256] = 6
common_mem[257] = 1
common_mem[258] = 13
common_mem[259] = 7
common_mem[260] = 8
common_mem[261] = -2
common_mem[262] = 7