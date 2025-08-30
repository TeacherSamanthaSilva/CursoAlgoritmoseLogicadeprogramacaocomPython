peso = float(input('Digite o peso da pesca em Kg: '))
excesso = peso - 50
multa = excesso * 4
print(f'Foram {excesso:.2f}Kg em excesso, logo, a multa é de R${multa:.2f}.')
