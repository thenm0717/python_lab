"""
📌 Description:
Напишите программу, которая считает стоимость трёх компьютеров, состоящих из монитора, системного блока, клавиатуры и мыши.
На вход программе подаются четыре целых числа (каждое на отдельной строке): стоимость монитора, стоимость системного блока, стоимость клавиатуры, стоимость мыши.

💡 Example output:
Sample Input -> 9900, 55600, 3999, 2990
Sample Output -> 217467

✅ My solution:
"""

monitor_price = int(input())
system_unit_price = int(input())
keyboard_price = int(input())
mouse_price = int(input())

total_price = 3 * (monitor_price + system_unit_price + keyboard_price + mouse_price)

print(total_price)