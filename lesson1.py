# 1.
word = "Tree"
number = 68
print(word, number)

word1 = input('Введите первое слово\n')
word2 = input('Введите второе слово\n')
word3 = input('Введите третье слово\n')
print("Теперь введите числа")
n1 = input('Введите первое число\n')
n2 = input('Введите второе число\n')
n3 = input('Введите третье число\n')

print("Слова в обратном порядке", word3, word2, word1)
print("Числа в обратном порядке", n3, n2, n1)

# 2.
number = input('Введите время в секундах\n')
number = int(number)
print('Время в привычном формате:', number // 3600, 'часов', (number - (number // 3600) * 3600) // 60,
      'минут', number - (number // 3600) * 3600 - ((number - (number // 3600) * 3600) // 60) * 60, 'секунд')

# 3.
n = int(input('Введите число\n'))
print(n + n * 10 + n + n * 100 + n * 10 + n)

# 4.
number = int(input('Введите число\n'))
maximum = number % 10
number = number // 10
while number > 1:
    if maximum < number % 10:
        maximum = number % 10
        number = number // 10
    else:
        number = number // 10

print('Самая большая цифра в числе:', maximum)

# 5.
n1 = int(input('Введите размер выручки фирмы\n'))
n2 = int(input('Введите размер издержек фирмы\n'))
if n1 - n2 > 0:
    print("Финансовый результат фирмы: прибыль")
    print("Рентабельность выручки:", n1 / (n1 - n2))
    number = int(input('Введите количество работников фирмы\n'))
    print("Прибыль фирмы в расчёте на одного сотрудника:", (n1 - n2) / number)
else:
    print("Финансовый результат фирмы: прибыль")

# 6.
n1 = int(input('Введите результат первого дня\n'))
n2 = int(input('Введите желаемый общий результат\n'))
number = 1
while n1 < n2:
    n1 = n1 + n1 * 0.1
    number += 1

print(number)
