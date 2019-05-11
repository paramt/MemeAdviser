from src import algorithm

def test_algorithm():
	algorithm.calculate(100, 5, 1000)
	algorithm.calculate(-100, -5, 1000)
	algorithm.calculate(5, 10, 1000)
	algorithm.break_even(100)
