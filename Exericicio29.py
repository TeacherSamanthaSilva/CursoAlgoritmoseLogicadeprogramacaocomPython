salarioAnterior = float(input("Digite seu salário atual: "))
salarioAtual = 0.0
diferencaEntreSalarios = 0.0
percentualDeAumento = 0.0
 
if salarioAnterior <= 280:
    percentualDeAumento = 20
elif salarioAnterior <= 750:
    percentualDeAumento = 15
elif salarioAnterior <= 1500:
    percentualDeAumento = 10
else:
    percentualDeAumento = 5
 
diferencaEntreSalarios = salarioAnterior * (percentualDeAumento / 100)
salarioAtual = salarioAnterior + diferencaEntreSalarios
print(f"Seu salário antes do reajuste era de R${salarioAnterior:.2f}")
print(f"Seu salário foi aumentado em {percentualDeAumento}%")
print(f"Seu salário foi aumentado em R${diferencaEntreSalarios:.2f}")
print(f"Seu salário atual é de R${salarioAtual:.2f}")