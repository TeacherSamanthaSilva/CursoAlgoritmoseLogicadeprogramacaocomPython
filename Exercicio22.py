letra = input('Digite uma letra: ').upper() #.upper() para deixar as letras maiúsculas, ficando assim mais fácil de comparar
 
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('Vogal')
else:
    print('Consoante')