#!/usr/bin/python3

# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

def display(i):
    return f"\033[38;5;{i}m{i:03}\033[0m \033[48;5;{i}m  \033[0m"

def batch(i, j):
    return " ".join(display(n) for n in range(i, j))

print(batch(0, 8))
print(batch(8, 16))
k = 6
for i in range(16, 256, k):
    print(batch(i, min(i + k, 255)))
