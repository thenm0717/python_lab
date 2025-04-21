"""
📌 Description:
Напишите программу, которая принимает на вход два числа "a" и "b", вычисляет сумму, разность и произведение для этих чисел и выводит текст в следующем формате:

<число a> + <число b> = <сумма чисел a и b>
<число a> - <число b> = <разность чисел a и b>
<число a> * <число b> = <произведение чисел a и b>

💡 Example output:
Sample Input -> 2, 8
Sample Output -> 
5 + 8 = 13
5 - 8 = -3
5 * 8 = 40

✅ My solution:
"""

num_a = int(input())
num_b = int(input())

print('%d + %d = %d' % (num_a, num_b, num_a + num_b))
print('%d - %d = %d' % (num_a, num_b, num_a - num_b))
print('%d * %d = %d' % (num_a, num_b, num_a * num_b))