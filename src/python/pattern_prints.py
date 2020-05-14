#!/usr/bin/env python3

def pattern(n: int, char: str):
    for i in range(1, n + 1):
        print(char * i)
    for i in range(1, n + 1):
        print(' ' * (n - i), char * i)
    for i in range(1, n + 1):
        print(' ' * (n - i), char * (1 + (2 * (i - 1))))
    for i in range(n, 0, -1):
        print(' ' * (n - i), char * (1 + (2 * (i - 1))))

pattern(12, '#')
