"""
📌 Description:
Программа перевода сантиметров в дюймы или наоборот

💡 Example output:
Sample Input -> 
Sample Output -> 

✅ My solution:
"""

num = float(input('Пожалуйста, введите длину: '))
unit = str(input('Пожалуйста, введите единицу измерения, если сантиметры - см, если дюймы - д: '))

if unit == 'см':
  print('%.2f сантиметр = %.2f дюйм' % (num, num / 2.54))
elif unit == 'д':
  print('%.2f дюйм = %.2f сантиметр' % (num, num * 2.54))
else:
    print('Пожалуйста, введите действительную единицу')