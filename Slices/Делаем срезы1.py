#На вход программе подается одна строка. Напишите программу, которая выводит:

#общее количество символов в строке;
#исходную строку, повторенную 3 раза;
#первый символ строки;
#первые три символа строки;
#последние три символа строки;
#строку в обратном порядке;
#строку с удаленным первым и последним символами.

s = input()

one = len(s)
two = s*3
three = s[0]
four = s[0:3]

five = s[-3:]

six = s[::-1]
seven = s[1:-1:]
print(one,two,three,four,five,six,seven, sep = '\n')
