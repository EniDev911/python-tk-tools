def calcular_imc(peso, altura):
	return round(peso/(altura**2), 2)

casos = [(50, 1.90), (80, 1.90), (100, 1.90), (120, 1.90)]


for caso in casos:
	#print(i)
	imc = calcular_imc(caso[0], caso[1])

	if imc < 18.0:
		print('BAJO PESO')

	elif imc <= 24.9:
		print('NORMAL')

	elif imc <= 29.9:
		print('SOBREPESO')
	else:
		print('OBESO')

