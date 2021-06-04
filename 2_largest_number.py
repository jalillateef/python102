numbers = [1, 50, 3, 99999, -100000, -2, 42]

highest = 0
for num in numbers:
    if num > highest:
        highest = num

print(highest)