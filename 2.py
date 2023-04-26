a=int(input('введите число: '))
b=int(input('степень числа: '))
def sum(a,b):
    if a==0:
        return(b)
    else:
        return(sum(a-1,b+1))
print('ответ: ',sum(a,b))