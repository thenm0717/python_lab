"""
📌 Description:
На вход программе подаются три натуральных числа: m(стартовое количество организмов), p(среднесуточное увеличение в 
%), n(количество дней для размножения.)

💡 Example output:
Sample Input -> 10, 50, 6
Sample Output -> 
✅ My solution:
"""

m = int(input())
p = int(input())
n = int(input())

for i in range(1, n + 1):
  result = m * (1 + p / 100) ** (i - 1)
  print(f'{i} {result}')