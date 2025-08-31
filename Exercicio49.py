populacao_A = 80_000
populacao_B = 200_000
anos = 0
while True:
    anos += 1
    populacao_A *= 1 + (3/100)
    populacao_B *= 1 + (1.5/100)
    if populacao_A >= populacao_B:
        print(
            f"Demorou {anos} anos para a população de A passar ou igualar a de B."
            f"\nA tem {populacao_A:.0f} habitantes e B tem {populacao_B:.0f}."
        )
        break