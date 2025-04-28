"""
📌 Description:
Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция» (без кавычек). Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!» (без кавычек).

💡 Example output:
Sample Input -> 25, 5, *
Sample Output -> 125

✅ My solution:
"""

number_1 = int(input())
number_2 = int(input())
operator = str(input())

if operator == '+':
  print(number_1 + number_2)
elif operator == '-':
  print(number_1 - number_2)
elif operator == '*':
  print(number_1 * number_2)
elif operator == '/':
  if number_2 == 0:
    print('На ноль делить нельзя!')
  else:
    print(number_1 / number_2)
else:
  print('Неверная операция')