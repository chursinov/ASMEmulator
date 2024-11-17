#Счётчик комманд
pc = 0

# Общая память
common_mem = [""] * 1024
cmd = ""

#память данных
DATA_BP = 256
data_pointer = 0

#прямой стэк - храним данные
STACK_BP = 512
stack_pointer = 8


#Обратный стек - храним указатели
REVERSE_STACK_BP = 768
reverse_stack_pointer = -1

# class stack(object):

#     def __init__(self, base_pointer, pointer) -> None:
#         self.base_pointer = base_pointer
#         self.pointer = pointer

#     def inc_pointer(self):
#         self.pointer += 1

#     def dcr_pointer(self):
#         self.pointer -= 1

# direct_stack = stack(STACK_BP, stack_pointer)
# reverse_stack = stack(REVERSE_STACK_BP, reverse_stack_pointer)

#Empty Flag - флаг пустого стэка
EF = 0
#Sign Flag - флаг знака. Загорается при результате сравнения < 0
SF = 0

common_mem[512] = 5
common_mem[513] = 7
common_mem[514] = 6
common_mem[515] = 3
common_mem[516] = 18
common_mem[517] = 9
common_mem[518] = 4
common_mem[519] = 0
common_mem[520] = -5