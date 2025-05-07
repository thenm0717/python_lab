"""
📌 Description:
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.



💡 Example output:
Sample Input -> 
Sample Output -> 3840
✅ My solution:
"""

total = 1

for i in range(1, 11):
  num = int(input())
  if num != 0:
    total *= num

print(total)