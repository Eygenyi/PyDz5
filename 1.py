a=int(input('введите число: '))
b=int(input('степень числа: '))
def stepen(a,b):
    if b==1:
        return(a)
    if b!=1:
        return(stepen(a,b-1)*a)
print('ответ: ',stepen(a,b))
