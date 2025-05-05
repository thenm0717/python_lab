"""
📌 Description:
Дано предложение и количество раз, сколько его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.

Программа должна вывести указанное текстовое предложение нужное количество раз. Каждое повторение должно начинаться с новой строки.

💡 Example output:
Sample Input -> Век живи - век учись, 10
Sample Output -> Век живи - век учись (10x)

✅ My solution:
"""

sentence = input('Sentence: ')
repeat_count = int(input('Count: '))

for i in range(repeat_count):
  print(sentence)