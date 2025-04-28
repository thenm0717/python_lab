"""
📌 Description:
Напишите программу, которая классифицирует треугольник на основе длин его сторон. Программа должна принимать три числа, каждое из которых представляет собой длину одной из его сторон. В результате программа должна определить, является ли треугольник равносторонним, равнобедренным или разносторонним.

💡 Example output:
Sample Input -> 145, 145, 149
Sample Output -> Равнобедренный

✅ My solution:
"""

side_a = int(input())
side_b = int(input())
side_c = int(input())

if side_a == side_b == side_c:
    print('Равносторонний')
elif side_a != side_b and side_b != side_c and side_a != side_c:
    print('Разносторонний')
else:
    print('Равнобедренный')