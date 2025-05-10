import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(mean_var_std.calculate([2,6,2,8,4,0,1,5,7]), {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[9.555555555555557, 2.6666666666666665, 10.222222222222221], [4.222222222222222, 10.666666666666666, 7.555555555555555], 8.987654320987654],
            'standard deviation': [[3.091206165165235, 1.632993161855452, 3.197221015541813], [2.0548046676563256, 3.265986323710904, 2.748737083745107], 2.998775336028987],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }, "Expected different result")
    
    def test_calculate_raises_error(self):
        with self.assertRaises(ValueError):
            mean_var_std.calculate([1,2,3,4,5,6,7,8])

if __name__ == "__main__":
    unittest.main()
