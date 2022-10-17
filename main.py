# ******************************
# Make your Code
# ******************************


numbers = list(map(int, input().split()))

for i in range(0, len(numbers)):
    min_=99999
    min_index = -1
    for j in range(i, len(numbers)):
        min_ = numbers[j]
        min_index = j
    temp = numbers[i]
    numbers[i] = min_
    numbers[min_index] = temp
    print(numbers)