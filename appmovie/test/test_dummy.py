from unittest import TestCase
from django.test import TestCase
from PIL.ImImagePlugin import number


########### Numeros Bouncy #################



def valida_bouncy(num):
    vali = num.isnumeric()
    if vali != str(vali): pass
    if vali is not number: print("La Exprecion no es un Numero Valido")

    return vali

#print(valida_bouncy("asas"))



def is_bouncy(num):

    nume = valida_bouncy(num)

    has_incr_seq, has_decr_seq = False, False
    right_digit = nume % 10
    nume = nume // 10

    while nume > 0:
        left_digit = nume % 10
        if left_digit < right_digit:
            has_incr_seq = True
        elif left_digit > right_digit:
            has_decr_seq = True
        right_digit = left_digit
        nume = nume // 10
        if has_incr_seq and has_decr_seq:
            return True
    return False

print(is_bouncy('casa33232"#"#$"#$'))

'''count = 0
i = 99
while count < 0.99 * i:
    i = i + 1
    if is_bouncy(i):
        count = count + 1

print(i)'''


'''for i in range(1000):
    print(i)
    if is_bouncy(i):
        print(i)
        pass
num = '123'''''

#############################################


class BouncyTest(TestCase):
    # Validando Cuano no es Bouncy
    def test_bouncy_frist_quits(self):
        assert not is_bouncy(100)
    # Validando Cuando lo es Bouncy
    def test_bouncy_two_quits(self):
        assert is_bouncy(101)
    #Validando Strings Bouncy
    def test_bouncy_three_quits(self):
        assert is_bouncy('101')
    # Validando String no Bouncy
    def test_bouncy_four_quits(self):
        assert not is_bouncy('100')
    # Validando numeros menores de 100
    def test_bouncy_five_quits(self):
        assert is_bouncy(23)










# palyndromes
'''def palindrome(string:str)->bool:
    return string.lower()[::-1]==string


class PalindromesTestCase(TestCase):
    def test_palindrome_function_should_return_true_for_anna(self):
        assert palindrome('anna')

    def test_palindrome_function_should_return_false_for_peter(self):
        assert not palindrome('peter')

    def test_palindrome_function_should_return_true_for_anna_capital_case(self):
        assert palindrome('Anna')'''

#------------------------ Ejemplo 1 -----------------------------
'''def add(x,y):
    return  x + y

class DummyTest(TestCase):


    def test_one_plus_one_is_two(self):
        assert add(1, 1) == 2, "one and one not true"

    def test_one_plus_two_is_three(self):
        #assert add(1, 2) == 3'''


