a = [7, 1, 3, 5, 8, 10, 25, 5]

max = a[0]
for pointer in range(len(a)):
    if a[pointer] > max:
        max = a[pointer]
print(max)