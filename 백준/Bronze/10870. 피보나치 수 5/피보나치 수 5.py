import sys

N = int(sys.stdin.readline().rstrip())

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(N))