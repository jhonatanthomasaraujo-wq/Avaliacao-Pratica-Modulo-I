import random
num_secreto = random.randrange(100,1000)
tentativas = 0
print("=======ADIVINHE O NUMERO SECRATO=======".CENTER(60))
print()
print("Digite 0 para sair a qualquer momento.\n")
while True:
    while True:
        entada = input("digite o numero com 3 dígitos: ")
    if entrada.isdigit() and(len(entrada)== 3 or entrada == "0")
        num = int(entrada)
        break
    else:
        print("entrada inválida, digite um numero"
              "de 3 digite")
        if num == 0:
            print("você decidiu  sair do jogo.Obrigado")
            exit()
        tentativa +=1
        if num == num_secreto:
            print(f"\nParabens!Você acertou o numero{num_secreto}.")
            print(f"O total de tentativas foi{tententativas}vezes.")
            break
        else:
            print("não acertou seu mané,tente novamente.")
            if num > num_secreto:
                print("Numero secreto é menor.")
            else:
                print("Numero secreto é Maior.")
     while True:
         resp = input("deseja jogar novamente?[s\n]".strip().lower()
            if resp == "n":
            print("Você decidiu sair .\n"
                      "obrigado por jogar.")
            break
        print ("até logo")
        
