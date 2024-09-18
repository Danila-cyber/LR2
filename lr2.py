#Натуральные числа, в которых строго чередуются четные и нечетные цифры. Список используемых в числах четных цифр выводить отдельно прописью. - Вариант 20
# Регулярные выражения

import re

pattern = r'^(?:(?:[13579][02468]|[02468][13579])*(?:[13579]|[02468])?)$'
dcCifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
fileName = "res.txt"

try:
  open(fileName, "r")
except:
  print("Файл отсутствует")

with open(fileName, 'r') as file:
    for line in file:
        numbers = line.split()  
        matchingNumbers = [num for num in numbers if re.fullmatch(pattern, num)]
        if matchingNumbers :
            for num in matchingNumbers :
                print(num)
                acceptChar = []
                for char in num:
                    if int(char) % 2 == 0: acceptChar.append(char)
                print("Четные цифры этого числа: " + ", ".join(list(map(lambda x: dcCifr [x], acceptChar))))
                print("____________________")


  
