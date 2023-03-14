base = int(input("Введите число: "))

exp = int(input("Введите степень: "))

def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))

print("Результат возведения в степень равен:", power(base, exp))