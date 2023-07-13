# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


HEXADECIMAL = 16
result = ''
number = int(input('Введите число для перевода в шестнадцатеричную систему: '))

while number > 1:
    devide = number % HEXADECIMAL
    if devide == 10:
        result += 'A'
    elif devide == 11:
        result += 'B'
    elif devide == 12:
        result += 'C'
    elif devide == 13:
        result += 'D'
    elif devide == 14:
        result += 'E'
    elif devide == 15:
        result += 'F'
    else:
        result = result + str(number % HEXADECIMAL)
    number = number // HEXADECIMAL
print(f'Результат: {result[::-1]}')



# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.


from math import gcd


fract1 = input('Введите первую дробь в формате a/b: ')
fract2 = input('Введите вторую дробь в формате a/b: ')
lst = fract1.split('/')
lst2 = fract2.split('/')
numerator1 = int(lst[0])
denominator1 = int(lst[1])
numerator2 = int(lst2[0])
denominator2 = int(lst2[1])

if denominator1 != denominator2:
    denom = denominator1 * denominator2
    summ = numerator1 * (denom / denominator1) + numerator2 * (denom / denominator2)
else:
    summ = numerator1 + numerator2
    denom = denominator1

numer_diff = numerator1 * numerator2
denom_diff = denominator1 * denominator2

gcd_numer_summ = gcd(int(summ), denom)
gcd_numer_diff = gcd(numer_diff, denom_diff)

reduced_summ = int(summ / gcd_numer_summ)
reduced_denom = int(denom / gcd_numer_summ)

reduced_numer_diff = int(numer_diff / gcd_numer_diff)
reduced_denom_diff = int(denom_diff / gcd_numer_diff)

print(f'Сумма: {reduced_summ}/{reduced_denom}')
print(f'Произведение: {reduced_numer_diff}/{reduced_denom_diff}')




