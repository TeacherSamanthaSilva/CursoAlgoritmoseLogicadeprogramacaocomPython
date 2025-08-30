nota1 = float(input('Digite a primeira nota do semestre: '))
nota2 = float(input('Digite a segunda nota do semestre: '))
 
media = (nota1 + nota2)/2
 
if media >= 9:
    aproveitamento = 'A'
elif media >= 7.5:
    aproveitamento = 'B'
elif media >= 6:
    aproveitamento = 'C'
elif media >= 4:
    aproveitamento = 'D'
else:
    aproveitamento = 'E'
    
if aproveitamento == 'D' or aproveitamento == 'E':
    print(f'REPROVADO\nAproveitamento: {aproveitamento}')
else:
    print(f'APROVADO\nAproveitamento: {aproveitamento}')