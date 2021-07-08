import unittest
import calcu_logic as cf


class Test(unittest.TestCase):
#--------------------BASIC_TEST------------------- 19
    def test_clear_all(self):
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.four()
        cf.clear_all()
        self.assertEqual(cf.calculate(), "0")

    def test_1plus1(self): # 1 + 1
        cf.clear_all()
        cf.one()
        cf.addition()
        cf.one()
        self.assertEqual(cf.calculate(), "2")

    def test_1trilplus1tril(self): # 1000000000000 + 10000000000001
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

    def test_5times4(self): # 5 * 4
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

    def test_0divide0(self):  # 0 / 0
        cf.clear_all()
        cf.zero()
        cf.division()
        cf.zero()
        self.assertEqual(cf.calculate(), "Math zero division error")

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

    def test_syntaxError_1(self):  # 5 ^^
        cf.clear_all()
        cf.five()
        cf.exponent()
        cf.exponent()
        cf.five()
        self.assertEqual(cf.calculate(), "Syntax error")

    def test_syntaxError_2(self):  # 5 // 5
        cf.clear_all()
        cf.five()
        cf.division()
        cf.division()
        cf.five()
        self.assertEqual(cf.calculate(), "Syntax error")

    def test_syntaxError_3(self):  # 5 +
        cf.clear_all()
        cf.five()
        cf.addition()
        self.assertEqual(cf.calculate(), "Syntax error")

    def test_syntaxError_4(self):  # 5 -
        cf.clear_all()
        cf.five()
        cf.subtraction()
        self.assertEqual(cf.calculate(), "Syntax error")

    def test_syntaxError_5(self):  # 5 *
        cf.clear_all()
        cf.five()
        cf.multiplication()
        self.assertEqual(cf.calculate(), "Syntax error")

#--------------------TRIGONOMETRY_TEST------------------- 15
    def test_sin(self):
        # sin5
        # 0.0871557427
        cf.clear_all()
        cf.sin();cf.five()
        
        self.assertEqual("0.0871557427", cf.calculate())

    def test_sin1(self):
        # sin90 + sin0 + sin270
        # 1 + 0 + 1 = 0
        cf.clear_all()
        cf.sin();cf.nine();cf.zero()
        cf.addition()
        cf.sin();cf.zero()
        cf.addition()
        cf.sin();cf.two();cf.seven();cf.zero()

        self.assertEqual("0.0", cf.calculate())

    def test_sin_sqrt(self):
        # sin√45 + sin45 + sin√45 + sin45
        # 0.1168129437 + sqrt2/2 + 0.1168129437 + sqrt2/2
        cf.clear_all()
        cf.sin();cf.sqrt();cf.four();cf.five()
        cf.addition()
        cf.sin();cf.four();cf.five()
        cf.addition()
        cf.sin();cf.sqrt();cf.four();cf.five()
        cf.addition()
        cf.sin();cf.four();cf.five()

        self.assertEqual("1.6478394498000002", cf.calculate())

    def test_sin_sqrt_pemdas(self):
        # sin0 + sin√180 - sin360 * sin√540 / sin64
        # 0 + 0.232026469 - 0 * 0.394549814 / 0.8987940463
        cf.clear_all()
        cf.sin();cf.zero()
        cf.addition()
        cf.sin();cf.sqrt();cf.one();cf.eight();cf.zero()
        cf.subtraction()
        cf.sin();cf.three();cf.six();cf.zero()
        cf.multiplication()
        cf.sin();cf.sqrt();cf.five();cf.four();cf.zero()
        cf.division()
        cf.sin();cf.six();cf.four()
        self.assertEqual("0.232026469", cf.calculate())

    def test_sin_sqrt_pemdas_parenthesis(self):
        # sin0 + (sin√180 - sin360) * sin√540 / sin64
        # 0 + (0.232026469 - 0) * 0.394549814 / 0.8987940463
        cf.clear_all()
        cf.sin();cf.zero()
        cf.addition()
        cf.parenthesis_open()
        cf.sin();cf.sqrt();cf.one();cf.eight();cf.zero()
        cf.subtraction()
        cf.sin();cf.three();cf.six();cf.zero()
        cf.parenthesis_close()
        cf.multiplication()
        cf.sin();cf.sqrt();cf.five();cf.four();cf.zero()
        cf.division()
        cf.sin();cf.six();cf.four()
        self.assertEqual("0.10185425745073359", cf.calculate())

    def test_cos(self):
        # cos5
        # 0.9961946981
        cf.clear_all()
        cf.cos();cf.five()
        
        self.assertEqual("0.9961946981", cf.calculate())

    def test_cos1(self):
        # cos90 + cos0 + cos270
        # 0 + 1 + 0 = 1
        cf.clear_all()
        cf.cos();cf.nine();cf.zero()
        cf.addition()
        cf.cos();cf.zero()
        cf.addition()
        cf.cos();cf.two();cf.seven();cf.zero()

        self.assertEqual("1.0", cf.calculate())

    def test_cos_sqrt(self):
        # cos√45 + cos45 + cos√45 + cos45
        # 0.9931539338 + sqrt2/2 + 0.9931539338 + sqrt2/2
        cf.clear_all()
        cf.cos();cf.sqrt();cf.four();cf.five()
        cf.addition()
        cf.cos();cf.four();cf.five()
        cf.addition()
        cf.cos();cf.sqrt();cf.four();cf.five()
        cf.addition()
        cf.cos();cf.four();cf.five()

        self.assertEqual("3.4005214300000004", cf.calculate())

    def test_cos_sqrt_pemdas(self):
        # cos0 + cos√180 - cos360 * cos√540 / cos64
        # 1 + 0.9727094724 - 1 * 0.918874553 / 0.4383711468
        cf.clear_all()
        cf.cos();cf.zero()
        cf.addition()
        cf.cos();cf.sqrt();cf.one();cf.eight();cf.zero()
        cf.subtraction()
        cf.cos();cf.three();cf.six();cf.zero()
        cf.multiplication()
        cf.cos();cf.sqrt();cf.five();cf.four();cf.zero()
        cf.division()
        cf.cos();cf.six();cf.four()
        self.assertEqual("-0.1234014594155517", cf.calculate())

    def test_cos_sqrt_pemdas_parenthesis(self):
        # cos0 + (cos√180 - cos360) * cos√540 / cos64
        # 1 + (0.9727094724 - 1) * 0.918874553 / 0.4383711468
        cf.clear_all()
        cf.cos();cf.zero()
        cf.addition()
        cf.parenthesis_open()
        cf.cos();cf.sqrt();cf.one();cf.eight();cf.zero()
        cf.subtraction()
        cf.cos();cf.three();cf.six();cf.zero()
        cf.parenthesis_close()
        cf.multiplication()
        cf.cos();cf.sqrt();cf.five();cf.four();cf.zero()
        cf.division()
        cf.cos();cf.six();cf.four()
        self.assertEqual("0.9427960267626261", cf.calculate())

    def test_tan(self):
        # tan5
        # 0.08748866353
        cf.clear_all()
        cf.tan();cf.five()
        
        self.assertEqual("0.0874886635", cf.calculate())

    def test_tan1(self):
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

    def test_tan_sqrt(self):
        # tan√45 + tan45 + tan√45 + tan45
        # 0.1176181654 + 1 + 0.1176181654 + 1
        cf.clear_all()
        cf.tan();cf.sqrt();cf.four();cf.five()
        cf.addition()
        cf.tan();cf.four();cf.five()
        cf.addition()
        cf.tan();cf.sqrt();cf.four();cf.five()
        cf.addition()
        cf.tan();cf.four();cf.five()

        self.assertEqual("2.2352363308", cf.calculate())

    def test_tan_sqrt_pemdas(self):
        # tan0 + tan√180 - tan360 * tan√540 / tan64
        # 1 + 0.9727094724 - 1 * 0.918874553 / 0.4383711468
        cf.clear_all()
        cf.tan();cf.zero()
        cf.addition()
        cf.tan();cf.sqrt();cf.one();cf.eight();cf.zero()
        cf.subtraction()
        cf.tan();cf.three();cf.six();cf.zero()
        cf.multiplication()
        cf.tan();cf.sqrt();cf.five();cf.four();cf.zero()
        cf.division()
        cf.tan();cf.six();cf.four()
        self.assertEqual("0.2385362491", cf.calculate())

    def test_tan_sqrt_pemdas_parenthesis(self):
        # tan0 + (tan√180 - tan360) * tan√540 / tan64
        # 0 + (0.2385362491 - 0) * 0.4293837638 / 2.050303842
        cf.clear_all()
        cf.tan();cf.zero()
        cf.addition()
        cf.parenthesis_open()
        cf.tan();cf.sqrt();cf.one();cf.eight();cf.zero()
        cf.subtraction()
        cf.tan();cf.three();cf.six();cf.zero()
        cf.parenthesis_close()
        cf.multiplication()
        cf.tan();cf.sqrt();cf.five();cf.four();cf.zero()
        cf.division()
        cf.tan();cf.six();cf.four()
        self.assertEqual("0.049955323871101874", cf.calculate())

#-------------------------------------Inverse Trigo------------------- 9
    def test_arcsin(self):
        cf.clear_all()
        cf.arcsin();cf.one()

        self.assertEqual("90.0", cf.calculate())

    def test_arcsin1(self):
        # arcsin1 + arcsin1
        # 90 + 90
        cf.clear_all()
        cf.arcsin();cf.one()
        cf.addition()
        cf.arcsin();cf.one()

        self.assertEqual("180.0", cf.calculate())

    def test_arcsin_sqrt(self):
        # arcsin1 + arcsin√1
        # 90 + 90
        cf.clear_all()
        cf.arcsin();cf.one()
        cf.addition()
        cf.arcsin();cf.sqrt();cf.one()

        self.assertEqual("180.0", cf.calculate())

    def test_arcsin_sqrt_log(self):
        # arcsin√log1
        cf.clear_all()
        cf.arcsin();cf.sqrt();cf.log();cf.one()

        self.assertEqual("0.0", cf.calculate())

    def test_arcsin_sqrt_ln(self):
        # arcsin√ln1
        cf.clear_all()
        cf.arcsin();cf.sqrt();cf.ln();cf.one()

        self.assertEqual("0.0", cf.calculate())

    def test_arcsin_sqrt_pemdas(self):
        # arcsin1 + arcsin√1 - arcsin1 * arcsin√1 / arcsin1
        cf.clear_all()
        cf.arcsin();cf.one()
        cf.addition()
        cf.arcsin();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arcsin();cf.one()
        cf.multiplication()
        cf.arcsin();cf.sqrt();cf.one()
        cf.division()
        cf.arcsin();cf.one()

        self.assertEqual("90.0", cf.calculate())

    def test_arcsin_sqrt_pemdas_decimal(self):
        # arcsin0.4 + arcsin√1 - arcsin1 * arcsin√1 / arcsin√0.3
        cf.clear_all()
        cf.arcsin();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arcsin();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arcsin();cf.one()
        cf.multiplication()
        cf.arcsin();cf.sqrt();cf.one()
        cf.division()
        cf.arcsin();cf.sqrt();cf.zero();cf.decimal();cf.three()

        self.assertEqual("-130.31757187680867", cf.calculate())

    def test_arcsin_sqrt_pemdas_decimal_pi(self):
        # arcsin0.4 + arcsin√1 - arcsin1 * arcsin√1 / arcsin√0.3 + pi
        cf.clear_all()
        cf.arcsin();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arcsin();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arcsin();cf.one()
        cf.multiplication()
        cf.arcsin();cf.sqrt();cf.one()
        cf.division()
        cf.arcsin();cf.sqrt();cf.zero();cf.decimal();cf.three()
        cf.addition()
        cf.pi()

        self.assertEqual("-127.17597922321887", cf.calculate())

    def test_arcsin_sqrt_pemdas_decimal_pi_parenthesis(self):
        # arcsin0.4 + arcsin√1 - arcsin1 * (arcsin√1 / arcsin√0.3 + pi)
        cf.clear_all()
        cf.arcsin();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arcsin();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arcsin();cf.one()
        cf.multiplication()
        cf.parenthesis_open()
        cf.arcsin();cf.sqrt();cf.one()
        cf.division()
        cf.arcsin();cf.sqrt();cf.zero();cf.decimal();cf.three()
        cf.addition()
        cf.pi()
        cf.parenthesis_close()

        self.assertEqual("-413.0609106998901", cf.calculate())

    def test_arcsin_sqrt_pemdas_decimal_pi_parenthesis_ln(self):
        # arcsin0.4 + arcsin√1 - arcsin√ln2 * (arcsin√1 / arcsin√0.3 + pi) - arcsinln2
        cf.clear_all()
        cf.arcsin();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arcsin();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arcsin();cf.sqrt();cf.ln();cf.two()
        cf.multiplication()
        cf.parenthesis_open()
        cf.arcsin();cf.sqrt();cf.one()
        cf.division()
        cf.arcsin();cf.sqrt();cf.zero();cf.decimal();cf.three()
        cf.addition()
        cf.pi()
        cf.parenthesis_close()
        cf.subtraction()
        cf.arcsin();cf.ln();cf.two()

        self.assertEqual("-260.10672917603864", cf.calculate())

    def test_arccos(self):
        cf.clear_all()
        cf.arccos();cf.one()

        self.assertEqual("0.0", cf.calculate())

    def test_arccos1(self):
        # arccos1 + arccos1
        # 0 + 0
        cf.clear_all()
        cf.arccos();cf.one()
        cf.addition()
        cf.arccos();cf.one()

        self.assertEqual("0.0", cf.calculate())

    def test_arccos_sqrt(self):
        # arccos1 + arccos√1
        # 0 + 0
        cf.clear_all()
        cf.arccos();cf.one()
        cf.addition()
        cf.arccos();cf.sqrt();cf.one()

        self.assertEqual("0.0", cf.calculate())

    def test_arccos_sqrt_log(self):
        # arccos√log1
        cf.clear_all()
        cf.arccos();cf.sqrt();cf.log();cf.one()

        self.assertEqual("90.0", cf.calculate())

    def test_arccos_sqrt_ln(self):
        # arccos√ln1
        cf.clear_all()
        cf.arccos();cf.sqrt();cf.ln();cf.one()

        self.assertEqual("90.0", cf.calculate())

    def test_arccos_sqrt_pemdas(self):
        # arccos1 + arccos√1 - arccos1 * arccos√1 / arccos1
        cf.clear_all()
        cf.arccos();cf.one()
        cf.addition()
        cf.arccos();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arccos();cf.one()
        cf.multiplication()
        cf.arccos();cf.sqrt();cf.one()
        cf.division()
        cf.arccos();cf.one()

        self.assertEqual("Math zero division error", cf.calculate())

    def test_arccos_sqrt_pemdas_decimal(self):
        # arccos0.4 + arccos√1 - arccos1 * arccos√1 / arccos√0.3
        cf.clear_all()
        cf.arccos();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arccos();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arccos();cf.one()
        cf.multiplication()
        cf.arccos();cf.sqrt();cf.one()
        cf.division()
        cf.arccos();cf.sqrt();cf.zero();cf.decimal();cf.three()

        self.assertEqual("66.42182152179817", cf.calculate())

    def test_arccos_sqrt_pemdas_decimal_pi(self):
        # arccos0.4 + arccos√1 - arccos1 * arccos√1 / arccos√0.3 + pi
        cf.clear_all()
        cf.arccos();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arccos();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arccos();cf.one()
        cf.multiplication()
        cf.arccos();cf.sqrt();cf.one()
        cf.division()
        cf.arccos();cf.sqrt();cf.zero();cf.decimal();cf.three()
        cf.addition()
        cf.pi()

        self.assertEqual("69.56341417538796", cf.calculate())

    def test_arccos_sqrt_pemdas_decimal_pi_parenthesis(self):
        # arccos0.4 + arccos√1 - arccos1 * (arccos√1 / arccos√0.3 + pi)
        cf.clear_all()
        cf.arccos();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arccos();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arccos();cf.one()
        cf.multiplication()
        cf.parenthesis_open()
        cf.arccos();cf.sqrt();cf.one()
        cf.division()
        cf.arccos();cf.sqrt();cf.zero();cf.decimal();cf.three()
        cf.addition()
        cf.pi()
        cf.parenthesis_close()

        self.assertEqual("66.42182152179817", cf.calculate())

    def test_arccos_sqrt_pemdas_decimal_pi_parenthesis_ln(self):
        # arccos0.4 + arccos√1 - arccos√ln2 * (arccos√1 / arccos√0.3 + pi) - arccosln2
        cf.clear_all()
        cf.arccos();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arccos();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arccos();cf.sqrt();cf.ln();cf.two()
        cf.multiplication()
        cf.parenthesis_open()
        cf.arccos();cf.sqrt();cf.one()
        cf.division()
        cf.arccos();cf.sqrt();cf.zero();cf.decimal();cf.three()
        cf.addition()
        cf.pi()
        cf.parenthesis_close()
        cf.subtraction()
        cf.arccos();cf.ln();cf.two()

        self.assertEqual("-85.37513000788404", cf.calculate())

    def test_arctan(self): # arctan1
        cf.clear_all()
        cf.arctan();cf.one()

        self.assertEqual("45.0", cf.calculate())

    def test_arctan1(self):
        # arctan1 + arctan1
        # 45 + 45
        cf.clear_all()
        cf.arctan();cf.one()
        cf.addition()
        cf.arctan();cf.one()

        self.assertEqual("90.0", cf.calculate())

    def test_arctan_sqrt(self):
        # arctan1 + arctan√1
        # 45 + 45
        cf.clear_all()
        cf.arctan();cf.one()
        cf.addition()
        cf.arctan();cf.sqrt();cf.one()

        self.assertEqual("90.0", cf.calculate())
    
    def test_arctan_sqrt_log(self):
        # arctan√log1
        cf.clear_all()
        cf.arctan();cf.sqrt();cf.log();cf.one()

        self.assertEqual("0.0", cf.calculate())

    def test_arctan_sqrt_ln(self):
        # arctan√ln1
        cf.clear_all()
        cf.arctan();cf.sqrt();cf.ln();cf.one()

        self.assertEqual("0.0", cf.calculate())

    def test_arctan_sqrt_pemdas(self):
        # arctan1 + arctan√1 - arctan1 * arctan√1 / arctan1
        cf.clear_all()
        cf.arctan();cf.one()
        cf.addition()
        cf.arctan();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arctan();cf.one()
        cf.multiplication()
        cf.arctan();cf.sqrt();cf.one()
        cf.division()
        cf.arctan();cf.one()

        self.assertEqual("45.0", cf.calculate())
    
    def test_arctan_sqrt_pemdas_decimal(self):
        # arctan0.4 + arctan√1 - arctan1 * arctan√1 / arctan√0.3
        cf.clear_all()
        cf.arctan();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arctan();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arctan();cf.one()
        cf.multiplication()
        cf.arctan();cf.sqrt();cf.one()
        cf.division()
        cf.arctan();cf.sqrt();cf.zero();cf.decimal();cf.three()

        self.assertEqual("-3.7302411598688536", cf.calculate())
    
    def test_arctan_sqrt_pemdas_decimal(self):
        # arctan0.4 + arctan√1 - arctan1 * arctan√1 / arctan√0.3 + pi
        cf.clear_all()
        cf.arctan();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arctan();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arctan();cf.one()
        cf.multiplication()
        cf.arctan();cf.sqrt();cf.one()
        cf.division()
        cf.arctan();cf.sqrt();cf.zero();cf.decimal();cf.three()
        cf.addition()
        cf.pi()

        self.assertEqual("-0.5886485062790605", cf.calculate())
    
    def test_arctan_sqrt_pemdas_decimal_pi_parenthesis(self):
        # arctan0.4 + arctans√1 - arctan1 * (arctan√1 / arctan√0.3 + pi)
        cf.clear_all()
        cf.arctan();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arctan();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arctan();cf.one()
        cf.multiplication()
        cf.parenthesis_open()
        cf.arctan();cf.sqrt();cf.one()
        cf.division()
        cf.arctan();cf.sqrt();cf.zero();cf.decimal();cf.three()
        cf.addition()
        cf.pi()
        cf.parenthesis_close()

        self.assertEqual("-145.10191057140952", cf.calculate())

    def test_arctan_sqrt_pemdas_decimal_pi_parenthesis_ln(self):
        # arctan0.4 + arctan√1 - arctan√ln2 * (arctan√1 / arctan√0.3 + pi) - arctanln2
        cf.clear_all()
        cf.arctan();cf.zero();cf.decimal();cf.four()
        cf.addition()
        cf.arctan();cf.sqrt();cf.one()
        cf.subtraction()
        cf.arctan();cf.sqrt();cf.ln();cf.two()
        cf.multiplication()
        cf.parenthesis_open()
        cf.arctan();cf.sqrt();cf.one()
        cf.division()
        cf.arctan();cf.sqrt();cf.zero();cf.decimal();cf.three()
        cf.addition()
        cf.pi()
        cf.parenthesis_close()
        cf.subtraction()
        cf.arctan();cf.ln();cf.two()

        self.assertEqual("-155.24515235478356", cf.calculate())

#------------------------------------Test logarithms-------------------- 10
    def test_e(self):
        # e
        cf.clear_all()
        cf.e()

        self.assertEqual("2.718281828459045", cf.calculate())

    def test_e1(self):
        # e + 4
        cf.clear_all()
        cf.e()
        cf.addition()
        cf.four()

        self.assertEqual("6.718281828459045", cf.calculate())

    def test_e_pemdas(self):
        # 5 * e + 3 + 3 - 10 / 2
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.e()
        cf.addition()
        cf.three()
        cf.addition()
        cf.three()
        cf.subtraction()
        cf.one()
        cf.zero()
        cf.division()
        cf.two()

        self.assertEqual("14.591409142295227", cf.calculate())

    def test_e_pemdas_parenthesis(self):
        # 5 * (e + 3) + 3 - 10 / 2
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.parenthesis_open()
        cf.e()
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

        self.assertEqual("26.591409142295223", cf.calculate())

    def test_e_pemdas_parenthesis_sqrt(self):
        # √5 * (e + 3) + 3 - 10 / 2 * √e
        cf.clear_all()
        cf.sqrt();cf.five()
        cf.multiplication()
        cf.parenthesis_open()
        cf.e()
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
        cf.multiplication()
        cf.sqrt();cf.e()

        self.assertEqual("7.542860529437416", cf.calculate())

    def test_ln(self):
        #lne + lne = 1 + 1 = 2
        cf.clear_all()
        cf.ln();cf.e()
        cf.addition()
        cf.ln();cf.e()

        self.assertEqual("2.0", cf.calculate())

    def test_ln1(self):
        #lne + lne - ln4 = 1 + 1 - 1.386294361 = 6
        cf.clear_all()
        cf.ln();cf.e()
        cf.addition()
        cf.ln();cf.e()
        cf.subtraction()
        cf.ln();cf.four()

        self.assertEqual("0.6137056389", cf.calculate())

    def test_ln_pemdas(self):
        # 5 * ln4 + 3 + ln3 - 10 / 2
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.ln();cf.four()
        cf.addition()
        cf.three()
        cf.addition()
        cf.ln();cf.three()
        cf.subtraction()
        cf.one()
        cf.zero()
        cf.division()
        cf.two()

        self.assertEqual("6.030084094199999", cf.calculate()) 

    def test_ln_e_pemdas(self):
        # 5 * lne + 3 + ln3 - 10 / 2
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.ln();cf.e()
        cf.addition()
        cf.three()
        cf.addition()
        cf.ln();cf.three()
        cf.subtraction()
        cf.one()
        cf.zero()
        cf.division()
        cf.two()

        self.assertEqual("4.0986122887", cf.calculate())

    def test_ln_e_pemdas_parenthesis(self):
        # 5 * lne + 3 + (ln3 - 10 / 2)
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.ln();cf.e()
        cf.addition()
        cf.three()
        cf.addition()
        cf.parenthesis_open()
        cf.ln();cf.three()
        cf.subtraction()
        cf.one();cf.zero()
        cf.division()
        cf.two()
        cf.parenthesis_close()

        self.assertEqual("4.0986122887", cf.calculate())

    def test_ln_e_pemdas_parenthesis_sqrt(self):
        # 5 * lne + 3 + (ln3 - 10 / 2) * √e
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.ln();cf.e()
        cf.addition()
        cf.three()
        cf.addition()
        cf.parenthesis_open()
        cf.ln();cf.three()
        cf.subtraction()
        cf.one();cf.zero()
        cf.division()
        cf.two()
        cf.parenthesis_close()
        cf.multiplication()
        cf.sqrt();cf.e()

        self.assertEqual("1.5676990951320988", cf.calculate())

    def test_ln_e_pemdas_parenthesis_sqrt_log(self):
        # 5 * lne + 3 + (ln3 - 10 / 2) * √e - √loge
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.ln();cf.e()
        cf.addition()
        cf.three()
        cf.addition()
        cf.parenthesis_open()
        cf.ln();cf.three()
        cf.subtraction()
        cf.one();cf.zero()
        cf.division()
        cf.two()
        cf.parenthesis_close()
        cf.multiplication()
        cf.sqrt();cf.e()
        cf.subtraction()
        cf.sqrt();cf.log();cf.e()

        self.assertEqual("0.9086888661520989", cf.calculate())

    def test_log(self):
        #log10 + log100 + log1000 + log10000 = 1 + 2 + 3 + 4 = 10.0
        cf.clear_all()
        cf.log();cf.one();cf.zero()
        cf.addition()
        cf.log();cf.one();cf.zero();cf.zero()
        cf.addition()
        cf.log();cf.one();cf.zero();cf.zero();cf.zero()
        cf.addition()
        cf.log();cf.one();cf.zero(); cf.zero(); cf.zero();cf.zero()

        self.assertEqual("10.0", cf.calculate())

    def test_log1(self):
        #log10 + log5
        cf.clear_all()
        cf.log();cf.one();cf.zero()
        cf.addition()
        cf.log();cf.five()

        self.assertEqual("1.6989700043", cf.calculate())

    def test_log_pemdas(self):
        # 5 * log7 + 3 + log3 - 10 / 2
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.log();cf.seven()
        cf.addition()
        cf.three()
        cf.addition()
        cf.log();cf.three()
        cf.subtraction()
        cf.one()
        cf.zero()
        cf.division()
        cf.two()

        self.assertEqual("2.7026114547000004", cf.calculate())

    def test_log_e_pemdas(self):
        # 5 * loge + 3 + log3 - 10 / 2
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.log();cf.e()
        cf.addition()
        cf.three()
        cf.addition()
        cf.log();cf.three()
        cf.subtraction()
        cf.one()
        cf.zero()
        cf.division()
        cf.two()

        self.assertEqual("0.6485936641999999", cf.calculate()) 

    def test_log_e_pemdas_parenthesis(self):
        # 5 * loge + 3 + (log3 - 10 / 2)
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.log();cf.e()
        cf.addition()
        cf.three()
        cf.addition()
        cf.parenthesis_open()
        cf.log();cf.three()
        cf.subtraction()
        cf.one();cf.zero()
        cf.division()
        cf.two()
        cf.parenthesis_close()

        self.assertEqual("0.6485936641999999", cf.calculate())

    def test_log_e_pemdas_parenthesis_sqrt(self):
        # 5 * loge + 3 + (log3 - 10 / 2) * √e
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.log();cf.e()
        cf.addition()
        cf.three()
        cf.addition()
        cf.parenthesis_open()
        cf.log();cf.three()
        cf.subtraction()
        cf.one();cf.zero()
        cf.division()
        cf.two()
        cf.parenthesis_close()
        cf.multiplication()
        cf.sqrt();cf.e()

        self.assertEqual("-2.285493982673038", cf.calculate())

    def test_log_e_pemdas_parenthesis_sqrt_ln(self):
        # 5 * loge + 3 + (log3 - 10 / 2) * √e - √lne
        cf.clear_all()
        cf.five()
        cf.multiplication()
        cf.log();cf.e()
        cf.addition()
        cf.three()
        cf.addition()
        cf.parenthesis_open()
        cf.log();cf.three()
        cf.subtraction()
        cf.one();cf.zero()
        cf.division()
        cf.two()
        cf.parenthesis_close()
        cf.multiplication()
        cf.sqrt();cf.e()
        cf.subtraction()
        cf.sqrt();cf.ln();cf.e()

        self.assertEqual("-3.285493982673038", cf.calculate())

#-----------------------------------test square root--------------------- 3
    def test_sqrt(self):
        #√40
        cf.clear_all()
        cf.sqrt(); cf.four(); cf.zero()

        self.assertEqual("6.324555320337", cf.calculate())

    def test_sqrt_decimal(self):
        #√25.25
        cf.clear_all()
        cf.sqrt() ; cf.two() ; cf.five()
        cf.decimal()
        cf.two(); cf.five()

        self.assertEqual("5.02493781056", cf.calculate())

    def test_sqrt_decimal_parenthesis(self):
        #√(25.25)
        cf.clear_all()
        cf.sqrt()
        cf.parenthesis_open()
        cf.two() ; cf.five()
        cf.decimal()
        cf.two(); cf.five()
        cf.parenthesis_close()

        self.assertEqual("5.02493781056", cf.calculate())

    def test_sqrt_pi(self):
        #√π
        cf.clear_all()
        cf.sqrt() ; cf.pi()

        self.assertEqual("1.772453850906", cf.calculate())

    def test_sqrt_e(self):
        #√e
        cf.clear_all()
        cf.sqrt();cf.e()

        self.assertEqual("1.6487212707", cf.calculate())

    def test_sqrt_ln_e(self):
        #√lne
        cf.clear_all()
        cf.sqrt();cf.ln();cf.e()

        self.assertEqual("1.0", cf.calculate())

    def test_sqrt_log_e(self):
        #√loge
        cf.clear_all()
        cf.sqrt();cf.log();cf.e()

        self.assertEqual("0.65901022898", cf.calculate())

 #-----------------------------------test for exponent--------------------- 
    def test_exponent(self):
         #2^2
         cf.clear_all()
         cf.two()
         cf.exponent() ; cf.two()
        
         self.assertEqual("4", cf.calculate())

    def test_exponent_decimal(self):
        #2.5^3
        cf.clear_all()
        cf.two();cf.decimal();cf.five()
        cf.exponent();cf.three()

        self.assertEqual("15.625", cf.calculate())

    def test_exponent_decimal_parenthesis(self):
        #(2.5)^3
        cf.clear_all()
        cf.parenthesis_open()
        cf.two();cf.decimal();cf.five()
        cf.parenthesis_close()
        cf.exponent();cf.three()

        self.assertEqual("15.625", cf.calculate())

    def test_exponent_pi(self):
        #π^2
        cf.clear_all()
        cf.pi()
        cf.exponent() ; cf.two()

        self.assertEqual("9.869604401089358", cf.calculate())


 #-----------------------------------test for pi--------------------- 
    def test_pi(self):
         #3π
         cf.clear_all()
         cf.three()
         cf.multiplication()
         cf.pi()

         self.assertEqual("9.42477796076938", cf.calculate())

    def test_sin_pi(self):
         #sinπ
         cf.clear_all()
         cf.sin() ; cf.pi()

         self.assertEqual("0.0548036651", cf.calculate())

    def test_log_pi(self):
         #logπ
         cf.clear_all()
         cf.log() ; cf.pi()

         self.assertEqual("0.4971498727", cf.calculate())    

    def test_tan_pi(self):
         #sinπ
         cf.clear_all()
         cf.tan() ; cf.pi()

         self.assertEqual("0.0548861508", cf.calculate()) 

#-------------------------------------------test for ANS-------------------- 2
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

#-------------------------------------------Test for syntax error-------------------- 2
    def text_syntax_error(self):
        cf.clear_all()
        cf.addition()
        cf.addition()
        cf.one()
        self.assertEqual("Syntax error", cf.calculate())

    def test_zero_divide(self):
        cf.clear_all
        cf.one()
        cf.division()
        cf.zero()
        self.assertEqual("Math zero division error", cf.calculate())

if __name__ == "__main__":
    unittest.main()