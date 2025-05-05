"""
📌 Description:
Даны два целых числа m и n. Напишите программу, которая выводит все целые числа от m до n включительно в порядке возрастания, если m < n, или в порядке убывания в противном случае.

💡 Example output:
Sample Input -> 
Sample Output -> 
✅ My solution:
"""

m = int(input())
n = int(input())

if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)
else:
    print(m)