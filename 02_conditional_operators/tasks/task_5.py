"""
📌 Description:
Назовём число красивым, если оно является четырёхзначным и делится нацело на  7 или на 17. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES» (без кавычек), если число является красивым, или «NO» (без кавычек) в противном случае.

💡 Example output:
Sample Input -> 1043
Sample Output -> YES

✅ My solution:
"""

num = int(input())

is_four_digit = 1000 <= num <= 9999
is_divisible = num % 7 == 0 or num % 17 == 0

if is_four_digit and is_divisible:
    print('YES')
else:
    print('NO')