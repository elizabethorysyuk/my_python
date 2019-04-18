num=int(input("Введите целое число:\n"))
def zel(num): return round(num)-num
def zel1(num): return 1-abs(zel(num))
num1=print(zel1(num))
def fun1(num1,m=2): return (num1)%m 
num2=print(fun1(num1))
if num1==1 and num2==0:
    print ("Число четное")
elif num1==1 and num2>0:
    print ("Число нечетное")
elif num1==1 and num2<0:
    print ("Число нечетное")
else:
    print ("Число не целое")
