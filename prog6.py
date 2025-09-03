numeros = []

for i in range(5):
    valor = int(input("Digite um número: "))
    numeros.append(valor)

busca = int(input("Digite o número que deseja buscar: "))

for n in numeros:
    if n == busca:
        print("Número encontrado!")
        break
else:
    print("Número não encontrado")