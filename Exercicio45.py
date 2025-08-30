carne = input("Digite F para filé duplo, A para alcatra e P para picanha: ")
peso = float(input("Digite quantos quilos dessa carne vai comprar: "))
pagamento = input("Dinheiro ou cartão tabajara (5% de desconto)? D ou C: ")
preco_total = 0
 
print("\nHipermercado Tabajara\nCupom fiscal\n")
if (carne == 'F' or carne == 'f'):
    print("Item: Filé Duplo")
    if (peso > 5):
        preco_total = peso * 5.8
    else:
        preco_total = peso * 4.9
elif (carne == 'A' or carne == 'a'):
    print("Item: Alcatra")
    if (peso > 5):
        preco_total = peso * 6.8
    else:
        preco_total = peso * 5.9
elif (carne == 'P' or carne == 'p'):
    print("Item: Picanha")
    if (peso > 5):
        preco_total = peso * 7.8
    else:
        preco_total = peso * 6.9
print(f"Quantidade: {peso:.2f}Kg")
print(f"Preço total: R${preco_total:.2f}")
if (pagamento == 'D' or pagamento == 'd'):
    print("Tipo de pagamento: Dinheiro")
    desconto = 0
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")
elif (pagamento == 'C' or pagamento == 'c'):
    print("Tipo de pagamento: Cartão Tabajara")
    desconto = preco_total * 5 / 100
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")