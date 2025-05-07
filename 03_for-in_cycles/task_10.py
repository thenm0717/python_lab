"""
📌 Description:
На вход программе подаётся натуральное число n.  Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно), квадрат которых оканчивается на 2, 5 или 8

💡 Example output:
Sample Input -> 100
Sample Output -> 500

✅ My solution:
"""

n = int(input())
total = 0

for i in range(1, n + 1):
  square = pow(i, 2)
  match square % 10:
    case 2 | 5 | 8:
      total += i

print(total)