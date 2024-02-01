import pytest


class Test_Math:
    def test_divide_number(self):
        pytest.xfail("Need to investigate")
        num = 10
        result = num + num
        assert result == num / num

    @pytest.mark.xfail(reason = "Result add numbers not multiply numbers")
    def test_square_number(self):
        num = 10
        result = num + num
        assert result == num ** 2

    @pytest.mark.xfail(reason = "Result & Assert are correct")
    def test_cube_number(self):
        num = 10
        result = num * num * num
        assert result == num ** 3

    @pytest.mark.xfail(run=False)
    def test_number_square(self):
        num = 10
        result = num * num  # 10 * 10 = 100
        assert result == num ** 2