def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))