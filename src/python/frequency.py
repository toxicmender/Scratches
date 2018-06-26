#!/usr/bin/env python3

import time

N = int(input("Size: "))
start = time.time()
s = []
d = dict()
end = time.time()
tm = (end - start)

for i in range(N):
    x = int(input("Element: "))
    start = time.time()
    if x in s:
        d[x] += 1
    else:
        s.append(x)
        d[x] = 1
    end = time.time()
    tm += (end - start)

Q = int(input("No. of Queries: "))
for i in range(Q):
    x = int(input("Query: "))
    start = time.time()
    if x in s:
        print(d[x])
    end = time.time()
    tm += (end - start)

print(tm)
