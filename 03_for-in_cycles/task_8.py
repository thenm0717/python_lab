"""
📌 Description:
Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n (от 1 до 10 включительно).


💡 Example output:
Sample Input -> 5
Sample Output -> 
✅ My solution:
"""

n = int(input())

for i in range(1, 11):
  print(f'{n} x {i} = {n * i}')