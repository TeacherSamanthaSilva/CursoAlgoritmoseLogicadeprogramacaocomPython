altura = float(input('Digite sua altura em metros: '))
pesoIdealHomem = (72.7 * altura) - 58
pesoIdealMulher = (62.1 * altura) - 44.7
print(f'O peso ideal para sua altura é:\n{pesoIdealHomem:.2f}Kg para homens.\n{pesoIdealMulher:.2f}Kg para mulheres.')