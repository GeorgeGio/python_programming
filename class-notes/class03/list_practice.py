numbers = [2,4,6,8]

print(max(numbers))

off_num = numbers.pop(-1)

print(off_num)
print(numbers)

numbers.insert(2,off_num)
print(numbers)

numbers.pop(1)

print(numbers)

numbers.append(3)

print(sum(numbers) / len(numbers))

print(numbers)
