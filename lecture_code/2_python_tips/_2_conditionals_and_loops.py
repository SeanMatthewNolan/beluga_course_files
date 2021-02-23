# Structure in Python is given by whitespace

# Conditionals

a = 4
if a < 5:
    print('a is less than 5')
elif a == 5:
    print('a is equal to 5')
else:
    print('a is greater than 5')


# While Loops
b = 0

while b < 10:
    print(b)
    b += 1

while b > 0:
    b -= 1
    if b == 7:
        continue
    elif b == 2:
        break
    print(b)

# For Loops
for item in [0, 'one', 2.]:
    print(item)

# Range
for idx in range(12):
    print(idx)

# Enumerate
for idx, item in enumerate([0, 'one', 2.]):
    print('{0:d}: {1}'.format(idx, item))

# Zip
for a, b in zip([1, 2, 3], [2, 3, 4]):
    print(a + b)

# List Comprehension

list1 = [k**2 for k in range(2, 10)]
list2 = [k**2 for k in range(10) if k > 3]

