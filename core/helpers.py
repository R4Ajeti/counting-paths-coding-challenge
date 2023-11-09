import math
def combination(n, k):
    if k > n - k:
        k = n - k

    combinationInt = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    return combinationInt