## 참고사이트: https://itstory1592.tistory.com/34

import sys

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(n):
  length = len(zero)
  if n >= length:
    for i in range(length, n+1):
      zero.append(zero[i-1] + zero[i-2])
      one.append(one[i-1] + one[i-2])
  print(zero[n], one[n])
  
T = int(sys.stdin.readline())

for _ in range(T):
  fibonacci(int(sys.stdin.readline()))