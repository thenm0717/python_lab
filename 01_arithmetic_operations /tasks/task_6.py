"""
📌 Description:
Напишите программу, которая рассчитывает сумму и произведение цифр положительного трёхзначного числа и выводит текст в следующем формате:

Сумма цифр = <сумма цифр>
Произведение цифр = <произведение цифр>

💡 Example output:
Sample Input -> 333
Sample Output -> Сумма цифр = 9
Произведение цифр = 27

✅ My solution:
"""

num = int(input())

hundreds = num // 100
tens = (num % 100) // 10
units = num % 10

sum_of_digits = hundreds + tens + units
product_of_digits = hundreds * tens * units

print(f"Сумма цифр = {sum_of_digits}")
print(f"Произведение цифр = {product_of_digits}")