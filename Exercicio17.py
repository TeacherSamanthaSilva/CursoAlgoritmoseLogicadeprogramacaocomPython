import math
metrosQuadrados = float(input('Digite os m²: '))
metrosQuadradosMaisDez = metrosQuadrados * 1.0
 
rendimentoLitro = 6
litrosLata = 18
precoLata = 80
rendimentoLata = rendimentoLitro * litrosLata
litrosGalao = 3.6
precoGalao = 25
rendimentoGalao = rendimentoLitro * litrosGalao
 
somenteLatas = math.ceil(metrosQuadrados / rendimentoLata)
somenteGaloes = math.ceil(metrosQuadrados / rendimentoGalao)
latas = math.floor(metrosQuadradosMaisDez / rendimentoLata)
galoes = math.ceil((metrosQuadradosMaisDez % rendimentoLata) / rendimentoGalao)
 
print(
    f'Somente Latas: {somenteLatas}, custando R${somenteLatas * precoLata}\n'
    f'Somente Galões: {somenteGaloes}, custando R${somenteGaloes * precoGalao}\n'
    f'Latas: {latas} , Galões: {galoes}, '
    f'custando R${((latas * precoLata) + (galoes *precoGalao)):.2f}')