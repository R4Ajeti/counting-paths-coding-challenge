from helpers import combination
from itertools import permutations

def countValidPaths(E, N):
    return combination(E+N, N)

def countValidRoots(freqOne, freqTwo):
    sentence = ""
    sentenceList = []
    availableLetters = "E"*freqOne + "N"*freqTwo

    for perm in set(permutations(availableLetters)):
        word = ''.join(perm)
        sentenceList.append(word)
    sentence = ', '.join(sentenceList)
    return sentence

def countPaths(east, north):
    validPathValue = countValidPaths(east, north)
    validRootValue = countValidRoots(east, north)
    return validPathValue, validRootValue

print("Valid paths: ", countPaths(2, 2))
print("Valid paths: ", countPaths(0, 7))
print("Valid paths: ", countPaths(0, 0))