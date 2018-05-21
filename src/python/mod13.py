#!usr/bin/python3

print("Years divisible by 13: ")
x = set([i for i in range(1989, 2999, 13)])
print(x, end="\n\n\r")

y = set([i for i in range(2028, 2999, 52)])
print(y, end="\n\n\r")

z = set([i for i in range(2000, 2999, 100)])
z.intersection_update(y)
print(z)
