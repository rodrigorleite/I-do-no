
alcool = float(input("Insira o valor do Alcool!: "))
gas = float(input("Insira o valor da Gasolina!: "))

resultado = alcool / gas

print(resultado)

if resultado > 0.9: 
    print("Vai de Shell V-Power: ")
elif resultado < 0.9: 
    print("Vai de Alcool: ")
else:
    print("Anota Anota!: ")