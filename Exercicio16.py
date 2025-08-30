import math
metrosQuadrados = float(input('Digite quantos metros quadrados você vai pintar: '))
latas = math.ceil(metrosQuadrados/54)
preco = latas * 80
print(f'Você precisa comprar {latas:.0f} lata(s), custando R${preco:.2f}')