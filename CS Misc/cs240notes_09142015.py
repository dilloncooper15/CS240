import math

def recur_fib(n):
	if (n < 2):
            return n
	if n not in fib:
            fib[n] = recur_fib(n - 2) + recur_fib(n - 1)
        return fib[n]

fib = {}
for i in range(0, 1000):
    print(recur_fib(i))
