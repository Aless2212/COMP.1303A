a = [2*x for x in range(1,10+1)]

print(a)

b = [2*x-1 for x in range(1,10+1)]
print(b)

print([n for n in range(1,10,2)])

print([0 if n % 3 == 0 else n for n in range(1, 10, 2)])

print([n if n % 3 != 0 else 0 for n in range(1, 10, 2)])