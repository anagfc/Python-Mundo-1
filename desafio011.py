altura = float(input('Altura da parede em metros: '))
largura = float(input('Largura da parede em metros: '))
areap = altura*largura
print('\nSua parede tem uma área de {}m².\nPara pintá-la, você precisará de {}L de tinta.'.format(areap, areap/2))
