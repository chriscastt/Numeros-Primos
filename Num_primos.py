def num_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

begin = int(input("Ingrese el inicio del rango: "))
end = int(input("Ingrese el fin del rango: "))

numeros_primos = [num for num in range(begin, end + 1) if num_primo(num)]

print(f"Los números primos en el rango de {begin} a {end} son:")
print(numeros_primos)