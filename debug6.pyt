numbers = [2, 3, 6, 6, 5]
freq = {}

for num in numbers:
    if num in freq:
        freq[num] = freq[num] + 1
    else:
        freq[num] = 1   # Bug: comparison instead of assignment

print("Number frequency:", freq)
