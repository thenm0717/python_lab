"""
📌 Description:
На вход программе подаётся натуральное число n. Напишите программу, которая для каждого из чисел от 
0 до n (включительно) выводит текст в следующем формате:

Квадрат числа <текущее число> равен <квадрат текущего числа>

💡 Example output:
Sample Input -> 9
Sample Output -> Квадрат числа 0 равен 0 ... Квадрат числа 9 равен 81

✅ My solution:
"""

sentence = input('Sentence: ')
repeat_count = int(input('Count: '))

n = int(input())

for i in range(n + 1):
  result = i ** 2
  print(f'Квадрат числа {i} равен {result}')