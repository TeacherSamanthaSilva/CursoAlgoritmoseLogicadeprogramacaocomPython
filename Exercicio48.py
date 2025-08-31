Nome = input('Digite o nome: ')
while len(nome) < 4:
    print('Nome inválido!')
    nome = nome = input('Digite o nome: ')
 
idade = int(input('Digite a idade: '))
while idade < 0 or idade > 150:
    print('Idade inválida!')
    idade = int(input('Digite a idade: '))
 
salario = int(input('Digite o salário: '))
while salario <= 0:
    print('Salario inválido!')
    salario = int(input('Digite a salário: '))
 
sexo = input('Digite o sexo (f ou m): ')
while sexo.lower() != 'f' and sexo.lower() != 'm':
    print('Sexo inválido!')
    sexo = input('Digite o sexo (f ou m): ')
 
estadoCivil = input('Digite o estado civil (s, c, v, d): ').lower()
while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
    print('Estado civil inválido!')
    estadoCivil = input('Digite o estado civil (s, c, v, d): ')