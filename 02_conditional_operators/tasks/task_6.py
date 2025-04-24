"""
📌 Description:
Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.

💡 Example output:
Sample Input -> 5, 2, 3
Sample Output -> NO

✅ My solution:
"""

side_a = int(input())
side_b = int(input())
side_c = int(input())

result_side_c = side_a + side_b > side_c
result_side_b = side_a + side_c > side_b
result_side_a = side_b + side_c > side_a

if result_side_a and result_side_b and result_side_c:
    print('YES')
else:
    print('NO')