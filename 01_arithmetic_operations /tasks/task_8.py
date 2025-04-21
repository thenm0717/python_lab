"""
📌 Description:
Напишите программу для нахождения цифр четырёхзначного числа.

💡 Example output:
Sample Input -> 3281
Sample Output -> 
Цифра в позиции тысяч равна 3
Цифра в позиции сотен равна 2
Цифра в позиции десятков равна 8
Цифра в позиции единиц равна 1

✅ My solution:
"""

num = int(input())

thousands = num // 1000
hundreds = (num % 1000) // 100 
tens = (num % 100) // 10  
units = num % 10  

print(f"Цифра в позиции тысяч равна {thousands}")
print(f"Цифра в позиции сотен равна {hundreds}")
print(f"Цифра в позиции десятков равна {tens}")
print(f"Цифра в позиции единиц равна {units}")