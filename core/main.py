from core.helpers import combination, filterStringsByConsecutiveChars
from itertools import permutations

def countValidPaths(E, N):
    return combination(E+N, N)

def countValidRoots(freqOne, freqTwo, exactlyThreeFlag=False):
    sentence = ""
    sentenceList = []
    availableLetters = "E"*freqOne + "N"*freqTwo

    for perm in set(permutations(availableLetters)):
        word = ''.join(perm)
        sentenceList.append(word)
    sentenceList.sort()
    if exactlyThreeFlag:
        sentenceList = filterStringsByConsecutiveChars(sentenceList)
    sentence = ', '.join(sentenceList)
    return sentence

def countPaths(east, north, exactlyThreeFlag=True):
    if type(east) is not int:
        raise TypeError("east must be an integer")
    if east < 0:
        raise ValueError("east must be a positive integer")
    if east > 1000:
        raise ValueError("east must be less than 1000")
    if type(north) is not int:
        raise TypeError("north must be an integer")
    if north < 0:
        raise ValueError("north must be a positive integer")
    if north > 1000:
        raise ValueError("north must be less than 1000")
    validPathValue = countValidPaths(east, north)
    validRootValue = countValidRoots(east, north, exactlyThreeFlag=exactlyThreeFlag)
    return validPathValue, validRootValue
