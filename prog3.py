valor = int(input("Digite o valor: "))

notas100 = valor // 100
valor %= 100

notas50 = valor // 50
valor %= 50

notas20 = valor // 20
valor %= 20

notas10 = valor // 10
valor %= 10

print("100:", notas100)
print("50 :", notas50)
print("20 :", notas20)
print("10 :", notas10)