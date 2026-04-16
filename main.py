import random

print("Bem vindo")

opcao = int(input("Selecione uma dificulade: "))

numero_escolhido = random.randint(1, 100)
chances = 0


if opcao == 1:
    print("Fácil")
    chances = 20
elif opcao == 2:
    print("Médio")
    chances = 10
elif opcao == 3:
    print("Difíil")
    chances = 5
else:
    print("Opção inválida")

while chances > 0:
    chute = int(input("Dê o seu chute: "))
    if chute == numero_escolhido:
        print(f"Parbéns! Você ganhou! O número era: {chute}")
        break
    else:
        print("Tente novamente!")
    chute -= 1
    
if numero_escolhido != chute:
    print(f"Você errou todas! O número era: {numero_escolhido}")