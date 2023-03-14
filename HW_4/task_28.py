a = int(input("Введите первое число: "))

b = int(input("Введите второе число: "))

def summa(a, b):
    a += 1
    b -= 1
    if b > 0:
        return summa(a, b)
    else:
        return a
 
print("Результат:", summa(a, b))
