def soma_valores(lista):
    total = 0
    for x in lista:
        total += x
    return total

numeros = []
for i in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)

resultado = soma_valores(numeros)
print("Soma =", resultado)