continuar = True
while continuar:
    populacao_A = float(input("Digite a população de A: "))
    populacao_B = float(input("Digite a população de B: "))
    crescimento_A = float(input("Digite o crescimento percentual da população de A: "))
    crescimento_B = float(input("Digite o crescimento percentual da população de B: "))
    anos = 0
    while True:
        anos += 1
        populacao_A *= 1 + (crescimento_A/100)
        populacao_B *= 1 + (crescimento_B/100)
        if populacao_A >= populacao_B:
            print(
                f"Demorou {anos} anos para a população de A passar ou igualar a de B."
                f"\nA tem {populacao_A:.0f} habitantes e B tem {populacao_B:.0f}."
            )
            break
    continuar = True if input("Deseja continuar (S/N)? > ").upper() == 'S' else False
