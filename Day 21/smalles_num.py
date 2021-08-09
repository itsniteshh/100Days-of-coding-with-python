smallest = 0

for num in [3, 55, 23, -14, 54, -1, 154, -45, 0]:
    if num < smallest:
        smallest = num
    print(smallest, num)

print(smallest)