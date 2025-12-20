arr = [0, 4, 0, 5]

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[pos] = arr[pos], arr[i]
        pos += 1

print(arr)


