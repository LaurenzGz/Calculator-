import unittest
import cf as cf


class Test(unittest.TestCase):
    def test_1plus1(self):
        cf.clear_all()
        cf.one()
        cf.addition()
        cf.one()
        self.assertEqual(cf.calculate(), 2)

    def test_1times1(self):
        cf.clear_all()
        cf.one()
        cf.multiplication()
        cf.one()
        self.assertEqual(cf.calculate(), 1)

    def test_5times4(self):
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.four()
        self.assertEqual(cf.calculate(), 20)

    def test_clear_all(self):
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.four()
        cf.clear_all()
        self.assertEqual(cf.calculate(), 0)

    def test_pemdas_1(self):# 5*5+3+3-10/2 = 26
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.five()
        cf.addition()
        cf.three()
        cf.addition()
        cf.three()
        cf.subtraction()
        cf.one()
        cf.zero()
        cf.division()
        cf.two()
        self.assertEqual(cf.calculate(), 26)

    def test_exponent_1(self): # 5^5 = 3125
        cf.clear_all()
        cf.five()
        cf.exponent()
        cf.five()
        self.assertEqual(cf.calculate(), 3125)

    def test_syntaxError_1(self): # 5^5 = 3125
        cf.clear_all()
        cf.five()
        cf.exponent()
        cf.exponent()
        cf.five()
        self.assertEqual(cf.calculate(), "Syntax error")

if __name__ == "__main__":
    unittest.main()
