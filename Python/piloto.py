print("Hello World!")

nota = float(input("Insira a primeira nota!: "))
nota2 = float(input("Insira a segunda nota!: "))
nota3 = float(input("Insira a terceira nota!: "))
nota4 = float(input("Insira a quarta nota!: "))

notafinal = (nota + nota2 + nota3 + nota4) / 4

print("A nota final é: ", notafinal)

if notafinal > 60:
    print("O aluno foi Aprovado (a): ")
elif(notafinal < 60):
    print("O aluno foi Reprovado (a): ")