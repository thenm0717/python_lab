"""
📌 Description:
Напишите программу, которая вычисляет объем куба и площадь его полной поверхности по введённому значению длины ребра.

💡 Example output:
Sample Input -> 25
Sample Output -> Объем = 15625
Площадь полной поверхности = 3750

✅ My solution:
"""

number = int(input())
cube_volume = number ** 3
cube_area = 6 * number ** 2

print(f'Объем = {cube_volume}')
print(f'Площадь полной поверхности = {cube_area}')