"""
📌 Description:
Преобразование 100-балльной системы в американскую систему оценок
90 баллов или более, выход A
80 баллов до 89 баллов, результат B
От 70 до 79 баллов, результат C
От 60 минут до 69 минут, выход D
Менее 60 баллов, вывод E

💡 Example output:
Sample Input -> 
Sample Output -> 

✅ My solution:
"""

score = int(input('Пожалуйста, введите оценку по стобальной системе: '))

if score >= 90:
  grade = 'A'
elif score >= 80:
  grade = 'B'
elif score >= 70:
  grade = 'C'
elif score >= 60:
  grade = 'D'
elif score < 60:
  grade = 'E'
print('Соответствующая оценка:', grade)