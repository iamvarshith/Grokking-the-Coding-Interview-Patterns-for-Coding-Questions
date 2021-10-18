array = [2, 3, 3, 3, 6, 9, 9]

temp = 0
count = 0
for i in range(len(array)):
    if temp == array[i]:
        array[i] = 0
        print(array)
        continue

    else:
        count += 1
    temp = array[i]


print(count)
print(array)