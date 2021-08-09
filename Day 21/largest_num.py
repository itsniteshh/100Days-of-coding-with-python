largest = -1
print("before", largest)
numbers = [9, 14, 55, 33, 53, 75, 43, 10]

for num in numbers:
    if num > largest:
        largest = num
    print(largest, num)


print("largest number after the test is", largest)