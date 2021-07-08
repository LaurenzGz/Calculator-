import unittest
import calcu_logic as cf


class Test(unittest.TestCase):
    def test_clear_all(self):
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.four()
        cf.clear_all()
        self.assertEqual(cf.calculate(), "0")

    def test_1plus1(self):
        cf.clear_all()
        cf.one()
        cf.addition()
        cf.one()
        self.assertEqual(cf.calculate(), "2")

    def test_1trilplus1tril(self):
        cf.clear_all()
        cf.one();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero()
        cf.addition()
        cf.one();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.zero();cf.one()
        self.assertEqual("20000000000001", cf.calculate())

    def test_0plus0(self):  # 0 + 0
        cf.clear_all()
        cf.zero()
        cf.addition()
        cf.zero()
        self.assertEqual(cf.calculate(), "0")

    def test_1minus1(self):  # 1 - 1
        cf.clear_all()
        cf.one()
        cf.subtraction()
        cf.one()
        self.assertEqual(cf.calculate(), "0")

    def test_0minus0(self):  # 0 - 0
        cf.clear_all()
        cf.zero()
        cf.subtraction()
        cf.zero()
        self.assertEqual(cf.calculate(), "0")

    def test_1times1(self):  # 1 * 1
        cf.clear_all()
        cf.one()
        cf.multiplication()
        cf.one()
        self.assertEqual(cf.calculate(), "1")

    def test_0times0(self):  # 0 * 0
        cf.clear_all()
        cf.zero()
        cf.multiplication()
        cf.zero()
        self.assertEqual(cf.calculate(), "0")

    def test_5times4(self):
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.four()
        self.assertEqual(cf.calculate(), "20")

    def test_1divide1(self):  # 1 / 1
        cf.clear_all()
        cf.one()
        cf.division()
        cf.one()
        self.assertEqual(cf.calculate(), "1.0")

    def test_pemdas_1(self):  # 5*5+3+3-10/2 = 26
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
        self.assertEqual(cf.calculate(), "26.0")

    def test_pemdas_parenthesis_1(self):  # 5*(5+3)+3-10/2 = 38
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.parenthesis_open()
        cf.five()
        cf.addition()
        cf.three()
        cf.parenthesis_close()
        cf.addition()
        cf.three()
        cf.subtraction()
        cf.one()
        cf.zero()
        cf.division()
        cf.two()
        self.assertEqual(cf.calculate(), "38.0")

    def test_exponent_1(self):  # 5^5 = 3125
        cf.clear_all()
        cf.five()
        cf.exponent()
        cf.five()
        self.assertEqual(cf.calculate(), "3125")

    def test_syntaxError_1(self):  # 5^5 = 3125
        cf.clear_all()
        cf.five()
        cf.exponent()
        cf.exponent()
        cf.five()
        self.assertEqual(cf.calculate(), "Syntax error")

    def test_syntaxError_1(self):  # 5 // 5
        cf.clear_all()
        cf.five()
        cf.division()
        cf.division()
        cf.five()
        self.assertEqual(cf.calculate(), "Syntax error")

#--------------------TRIGONOMETRY_TEST-------------------
    def test_sin(self):
        # sin90 + sin0 + sin270
        # 1 + 0 -1 = 0
        cf.clear_all()
        cf.sin();cf.nine();cf.zero()
        cf.addition()
        cf.sin();cf.zero()
        cf.addition()
        cf.sin();cf.two();cf.seven();cf.zero()

        self.assertEqual("0.0", cf.calculate())

    def test_sin_1(self):
        # sin45 + sin45 + sin45 + sin45
        # sqrt2/2 + sqrt2/2 + sqrt2/2 + sqrt2/2
        cf.clear_all()
        cf.sin();cf.four();cf.five()
        cf.addition()
        cf.sin();cf.four();cf.five()
        cf.addition()
        cf.sin();cf.four();cf.five()
        cf.addition()
        cf.sin();cf.four();cf.five()

        self.assertEqual("2.8284271248", cf.calculate())

    def test_sin_2(self):
        # sin0 + sin180 + sin360 + sin540 + sin720 + sin900
        # sqrt2/2 + sqrt2/2 + sqrt2/2 + sqrt2/2
        cf.clear_all()
        cf.sin();cf.zero()
        cf.addition();cf.sin();cf.one();cf.eight();cf.zero()
        cf.addition()
        cf.sin();cf.three();cf.six();cf.zero()
        cf.addition()
        cf.sin();cf.five();cf.four();cf.zero()
        cf.addition()
        cf.sin();cf.seven();cf.two();cf.zero()
        cf.addition()
        cf.sin();cf.nine();cf.zero();cf.zero()
        self.assertEqual("0.0", cf.calculate())

    def test_cos(self):
        # cos90 + cos0 + cos270
        # 0 + 1 -0 = 1
        cf.clear_all()
        cf.cos();cf.nine();cf.zero()
        cf.addition()
        cf.cos();cf.zero()
        cf.addition()
        cf.cos();cf.two();cf.seven();cf.zero()

        self.assertEqual("1.0", cf.calculate())

    def test_tan(self):
        # tan45 + tan0 + tan405 + tan765
        # 1 + 0 + 1 + 1 = 3
        cf.clear_all()
        cf.tan();cf.four();cf.five()
        cf.addition()
        cf.tan();cf.zero()
        cf.addition()
        cf.tan();cf.four();cf.zero();cf.five()
        cf.addition()
        cf.tan();cf.seven();cf.six();cf.five()

        self.assertEqual("3.0", cf.calculate())
#-------------------------------------Inverse Trigo-------------------
    def test_arctan(self):
        cf.clear_all()
        cf.arctan();cf.one()

        self.assertEqual("45.0", cf.calculate())

    def test_arcsin(self):
        cf.clear_all()
        cf.arcsin();cf.one()

        self.assertEqual("90.0", cf.calculate())

    def test_arccos(self):
        cf.clear_all()
        cf.arccos();cf.one()

        self.assertEqual("0.0", cf.calculate())
#------------------------------------Test logarithms--------------------
    def test_e(self):
        # e + e
        # 1 + 0 + 1 + 1 = 3
        cf.clear_all()
        cf.e()
        cf.addition()
        cf.e()

        self.assertEqual("5.43656365691809", cf.calculate())

    def test_ln(self):
        #lne + lne = 1 + 1 = 2
        cf.clear_all()
        cf.ln();cf.e()
        cf.addition()
        cf.ln();cf.e()

        self.assertEqual("2.0", cf.calculate())

    def test_log(self):
        #log10 + log100 + log1000 + log10000 = 1 + 2 + 3 + 4 = 10.0
        cf.clear_all()
        cf.log();cf.one();cf.zero()
        cf.addition()
        cf.log();cf.one();cf.zero();cf.zero()
        cf.addition()
        cf.log();cf.one();cf.zero();cf.zero();cf.zero();
        cf.addition()
        cf.log();cf.one();cf.zero(); cf.zero(); cf.zero();cf.zero();

        self.assertEqual("10.0", cf.calculate())
#-----------------------------------test square root
    def test_sqrt(self):
        #2 + 3 = 5.0
        cf.clear_all()
        cf.sqrt() ; cf.two() ; cf.five()
        cf.decimal()
        cf.two(); cf.five()

        self.assertEqual("5.02493781056", cf.calculate())
#-------------------------------------------test for ANS--------------------
    def test_ans(self):
        #2 + 3 = 5.0
        cf.clear_all()
        cf.one() ; cf.addition() ; cf.one()
        cf.calculate()
        cf.ans(); cf.addition(); cf.three()

        self.assertEqual("5", cf.calculate())

    def test_ans_2(self):
        #2 + 3 = 5.0
        cf.clear_all()
        cf.one() ; cf.addition() ; cf.one()
        cf.calculate()
        cf.ans(); cf.addition(); cf.three(); cf.addition(); cf.ans()
        cf.addition() ; cf.ans()
        self.assertEqual("9", cf.calculate())

#-------------------------------------------Test for syntax error--------------------
    def text_syntax_error(self):
        cf.clear_all()
        cf.plus()
        cf.plus()
        cf.one()
        self.assertEqual("Syntax error", cf.calculate())

    def test_zero_divide(self):
        cf.clear_all
        cf.one()
        cf.division()
        cf.zero()
        self.assertEqual("Math zero divison error", cf.calculate())

if __name__ == "__main__":
    unittest.main()