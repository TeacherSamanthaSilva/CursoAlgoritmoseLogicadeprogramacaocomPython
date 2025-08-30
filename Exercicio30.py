valorDaHora = float(input("Digite quanto você recebe por hora: "))
horasTrabalhadas = float(input("Digite quantas horas você trabalhou esse mês: "))
salarioBruto = valorDaHora * horasTrabalhadas
if salarioBruto <= 900:
    descontoIr = 0.0
elif salarioBruto <= 1500:
    descontoIr = 5
elif salarioBruto <= 2500:
    descontoIr = 10
else:
    descontoIr = 20
 
IR = salarioBruto * (descontoIr / 100)
INSS = salarioBruto * (10 / 100)
FGTS = salarioBruto * (11 / 100)
totalDeDescontos = IR + INSS
salarioLiquido = salarioBruto - totalDeDescontos
 
print(
    f'\nSalário Bruto     : R${salarioBruto:.2f}',
    f'\n(-) IR (5%)       : R${IR:.2f}',
    f'\n(-) INSS ( 10%)   : R${INSS:.2f}',
    f'\nFGTS (11%)        : R${FGTS:.2f}',
    f'\nTotal de descontos: R${totalDeDescontos:.2f}',
    f'\nSalário Liquido   : R${salarioLiquido:.2f}'
)