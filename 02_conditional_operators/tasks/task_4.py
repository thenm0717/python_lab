"""
📌 Description:
Напишите программу, которая принимает целое число X и определяет, принадлежит ли данное число указанным промежуткам.

💡 Example output:
Sample Input -> -332
Sample Output -> Не принадлежит

✅ My solution:
"""

x = int(input())

if (x > -30 and x <= -2) or (x > 7 and x <= 25):
    print('Принадлежит')
else:
    print('Не принадлежит')