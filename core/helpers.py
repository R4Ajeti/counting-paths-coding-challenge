import math
def combination(n, k):
    if k > n - k:
        k = n - k

    combinationInt = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    return combinationInt

def filterStringsByConsecutiveChars(inputList):
    filteredList = []

    for string in inputList:
        for i in range(len(string) - 2):
            if string[i] == string[i + 1] == string[i + 2]:
                filteredList.append(string)
                break

    return filteredList