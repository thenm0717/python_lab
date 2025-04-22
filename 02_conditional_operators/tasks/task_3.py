"""
📌 Description:
Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
💡 Example output:
Sample Input -> 1614
Sample Output -> ДА

✅ My solution:
"""

num = int(input())

first_digit = num // 1000
second_digit = (num % 1000) // 100
third_digit = (num % 100) // 10
last_digit = num % 10

if (first_digit + last_digit) == (second_digit - third_digit):
  print('ДА')
else:
  print('НЕТ')