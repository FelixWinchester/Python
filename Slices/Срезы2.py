#На вход программе подается одна строка. Напишите программу, которая выводит:

#третий символ этой строки;
#предпоследний символ этой строки;
#первые пять символов этой строки;
#всю строку, кроме последних двух символов;
#все символы с четными индексами;
#все символы с нечетными индексами;
#все символы в обратном порядке;
#все символы строки через один в обратном порядке, начиная с последнего.


s = input()

one = s[2]
two = s[-2]
three = s[:5]
four = s[:-2]
five = s[::2]


six = s[1::2]


seven = s[::-1]
eight = s[::-2]

print(one,two,three,four,five,six,seven,eight, sep = '\n')
