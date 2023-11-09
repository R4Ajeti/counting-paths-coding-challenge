import pytest
from core.main import countValidRoots

class TestCountValidRoots:

    # Returns a string of all possible permutations of "E" and "N" characters when given valid input values for freqOne and freqTwo
    def testCountValidRoots(self):
        assert countValidRoots(2, 2) == "EN, NE, EE, NN"
        assert countValidRoots(0, 7) == "NNNNNNN"
        assert countValidRoots(1, 3) == "ENNN, NENN, NNEN, NNNE"
        assert countValidRoots(3, 1) == "EENN, ENEN, ENNE, NENE, NNEE, NEEE"
        assert countValidRoots(0, 4) == "NNNN"
        assert countValidRoots(4, 0) == "EEEE"

    # Returns an empty string when given input values of 0 for freqOne and freqTwo
    def testCountValidRootsZero(self):
        assert countValidRoots(0, 0) == ""

    # Returns a string of "E" characters when given an input value of 1 for freqOne and 0 for freqTwo
    def testSingleMove(self):
        assert countValidRoots(1, 0) == "E"

    