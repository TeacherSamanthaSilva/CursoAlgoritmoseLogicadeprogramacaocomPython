tamanho = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade da conexão em Mbps: '))
tempos = (tamanho * 8) / velocidade
minutos = tempos // 60
segundos = (tempos % 60)
print(f'{minutos:.0f} Minutos e {segundos:.0f} Segundos')