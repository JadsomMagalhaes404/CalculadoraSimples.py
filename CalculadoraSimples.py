print("Inicio do programa")

def adicao(a, p):
    return a + p
def subtracao(a, p):
    return a - p
def divisao(a, p):
    return a / p
def multiplicacao(a, p):
    return a * p
controle = True
while controle == True:
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    print("\nDigite uma das seguintes letras para realizar a operação que deseja!")
    print("\nA = Adição", "\nB = Subtração", "\nC = Divisão", "\nD = Multiplicação,","\nE = Sair")
    letra = input("Digite a letra correspondente a função que você deseja: ").upper()
    if letra == "A":
        res = adicao(n1, n2)
        print(f"{n1} + {n2} = {res}")
    elif letra == "B":
        res = subtracao(n1, n2)
        print(f"{n1} - {n2} = {res}")
    elif letra == "C":
        res = divisao(n1, n2)
        print(f"{n1} / {n2} = {res}")
    elif letra == "D":
        res = multiplicacao(n1, n2)
        print(f"{n1} x {n2} = {res}")
    elif letra == "E":
        print("Você saiu do programa")
        controle = False
    else:
        print("Opção invalida")
        controle = False

    