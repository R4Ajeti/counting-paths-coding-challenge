import pytest
from core.main import countValidPaths

class TestCountValidPaths:

    # Returns a valid int for paths when given valid input values for freqOne and freqTwo
    def testCountValidPaths(self):
        assert countValidPaths(2, 2) == 6
        assert countValidPaths(0, 7) == 1
        assert countValidPaths(1, 3) == 4
        assert countValidPaths(3, 1) == 4
        assert countValidPaths(0, 4) == 1
        assert countValidPaths(4, 0) == 1
    
    # Returns 1 when given input values of 0
    def testCountValidPathsZero(self):
        assert countValidPaths(0, 0) == 1

    # Returns valid int value for input values of 999.
    def testCountValidPathsMax(self):
        assert countValidPaths(10**3-1, 10**3-1) == 145438911035517264555381561230116189292650837306095363076178842645481320822198226994485371813976409145438911035517264676367032381831285411152247284028125396742405627998638503788368259307920236258027800099771751391617411152247284028125605088924033394630230806037178021722568614945945597158227817488131642780881551702876651234929533423568614945945597158690387735417418121162690198676382656195692212519230804188796272372873746380773141117366928488415626188796272372873746459630446598074332450038402866155063023175006229242447751399777865500335793470023989772130248615305793470023989772130440000