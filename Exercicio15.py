precoHora = float(input('Digite quanto você ganha por hora: '))
horasTrabalhadas = float(input('Digite quantas horas você trabalhou esse mês: '))
salarioBruto = precoHora * horasTrabalhadas
IR = salarioBruto * (11/100)
INSS = salarioBruto * (8/100)
sindicato = salarioBruto * (5/100)
salarioLiquido = salarioBruto - IR - INSS - sindicato
print(f'+ Salário Bruto : R${salarioBruto:.2f}')
print(f'- IR (11%) : R${IR:.2f}')
print(f'- INSS (8%) : R${INSS:.2f}')
print(f'- Sindicato (5%) : R${sindicato:.2f}')
print(f'= Salário Liquido : R${salarioLiquido:.2f}')
