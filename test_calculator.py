from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):

        a = 4321
        b = 1234
        cal = Calculator()

        result = cal.add(a, b)

        expected = 5555
        assert result == expected

    def test_subtract (self):
    # arrange
        a = 4321
        b = 1234
        cal = Calculator()

    # act
        result = cal.subtract (a, b)

    # assert
        expected = 3087
        assert result == expected

