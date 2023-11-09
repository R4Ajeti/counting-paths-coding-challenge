import pytest
from core.main import countPaths

class TestCountPaths:
    # Returns valid path value and valid root value for valid input values.
    def testValidInputValues(self):
        result = countPaths(5, 3)
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], int)
        assert isinstance(result[1], str)

    # Returns valid path value and valid root value for input values of 0.
    def testZeroInputValues(self):
        result = countPaths(0, 0)
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], int)
        assert isinstance(result[1], str)
    
    # Raises a ValueError when given negative input values for East and North
    def testNegativeInput(self):
        with pytest.raises(ValueError):
            countPaths(-1, 2)
        with pytest.raises(ValueError):
            countPaths(3, -2)
        with pytest.raises(ValueError):
            countPaths(-4, -4)

    # Raises a TypeError when given non-integer input values for East and North
    def testNonIntegerInput(self):
        with pytest.raises(TypeError):
            countPaths("2", 3)
        with pytest.raises(TypeError):
            countPaths(4, 2.5)
        with pytest.raises(TypeError):
            countPaths(True, False)

    # Raises a ValueError when given input values that exceed the maximum input value for East and North
    def testMaxIntegerInput(self):
        with pytest.raises(ValueError):
            countPaths(10**3+1, 10**3+1)