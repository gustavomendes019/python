import random

#lista de time de futebol
times = [
    "barcelona de itaquera",
    "Flamengo",
    "Cruzeiro",
    "Ibis",
    "RDS futsal",
    "Time da esquina",
    "Seleçao de cegos",
    "Palmeiras"
]

#Pontuaçao inicial
pontuaçao = {}

for time in times:
    pontuaçao[time] = 0

    # Frase inicial
    print("=== FACE MASH DE TIMES ===")
    print("escolha o melhor time!\n")

    # Quantidade de rodadas 
    for rodada in range(5):
        #escolha 2 times
        time1, time2 = random.sample(times, 2)

        print(f"rodada {rodada + 1}")
        print("1 - ", time1)
        print("2 -", time2)

        escolha = input("Escolha (1 ou 2): ")

        if escolha == "1":
            pontuaçao[time1] +=1
            print("Voce escolheu {time}\n")
        elif escolha == "2":
                                pontuaçao[time2] +=1
        print("Voce escolheu {time}\n")
    else:
            print("Opçao invalida!\n")

            #mostra o ranking final]

    print("=== RANKING FINAL ===") 
    ranking = sorted(
        pontuaçao.items(),
        key=lambda item: item[1],
        reverse=True

    )           
    
    for time, pontos in ranking:
        print(f"{time}:  {pontos} votos")