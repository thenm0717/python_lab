"""
📌 Description:
На вход программе подаются два целых числа a и b.Напишите программу, которая подсчитывает количество чисел в диапазоне от 
a до b (включительно), куб которых оканчивается на 4 или 9

💡 Example output:
Sample Input -> 1, 10
Sample Output -> 2

✅ My solution:
"""

a = int(input())
b = int(input())
counter = 0

for i in range(a, b + 1):
  cube = pow(i, 3)
  if cube % 10 == 4 or cube % 10 == 9:
    counter += 1

print(counter)