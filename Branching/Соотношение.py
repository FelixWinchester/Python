number = int(input())

uno = number // 1000
dos = number // 100 % 10
tres = number // 10 % 10
quadro = number % 10 

summ = uno + quadro
dis = dos - tres

if (summ == dis ):
    print("Yes")
else:
    print("No")
