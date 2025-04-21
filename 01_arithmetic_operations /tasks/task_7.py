"""
📌 Description:
Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.

💡 Example output:
Sample Input -> 123
Sample Output -> 123, 132, 213, 231, 312, 321

✅ My solution:
"""

num = int(input())

hundreds = num // 100 
tens = (num % 100) // 10  
units = num % 10  

print(hundreds, tens, units, sep='', end='\n')
print(hundreds, units, tens, sep='', end='\n')
print(tens, hundreds, units, sep='', end='\n')
print(tens, units, hundreds, sep='', end='\n')
print(units, hundreds, tens, sep='', end='\n')
print(units, tens, hundreds, sep='', end='\n')