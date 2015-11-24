
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

# list.pop()_removes and returns the item
# [1, 2, 3, 4, 5]
# If we do not specify which number in list.pop(), pop will choose the last\
    # number which, in this case, is 5.
