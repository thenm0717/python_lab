"""
📌 Description:
Напишите программу вывода на экран трёх последовательно идущих чисел, каждое на отдельной строке. 
Первое число вводит пользователь, остальные числа вы должны сами вычислять в программе.

💡 Example output:
Sample Input -> 8
Sample Output -> 8, 9, 10

✅ My solution:
"""

user_num = int(input(''))
first_num = user_num + 1
second_num = first_num + 1

print(user_num, first_num, second_num, sep=('\n'))