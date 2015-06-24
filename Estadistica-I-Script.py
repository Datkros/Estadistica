import math
from tabulate import tabulate

def obtiene_numeros(): # Pide los numeros y los guarda en una lista.
	global lst
	lst = []
	contador = 0
	try:
		cantidad_datos = int(raw_input("Ingrese la cantidad de datos de la distribucion: "))
		while contador < cantidad_datos:
			try:
				number = int(raw_input("Ingrese los datos: "))
				lst.append(number)
				contador += 1
			except:
				print "Por favor ingrese un valor numerico."
		lst.sort()
	except:
		print "Por favor ingrese un valor numerico."
	return lst
		

def suma_numeros(): #Calcula la suma de todos los valores
	global product
	product = 0
	for Value in lst: 
		product += Value
	return product

def pow_numbers(): #Calcula la sumatoria de todos los valores al cuadrado.
	temp = 0
	for i in lst:
		temp += (i - mediaPoblacional)**2

def atr_ic(): # Calcula la amplitud total real y el valor del intervalo de clase.
	global IC
	global valorMayor
	valorMayor = max(lst)
	valorMenor = min(lst)
	ATR = valorMayor - valorMenor + 1
	IC = ATR / round((1 + 3.322 * math.log10(len(lst))))
	IC = int(round(IC))

def intervalos_de_clase(IC, lst): # Genera una lista de los intervalos de clase.
	global listaIntervalos
	listaIntervalos = []
	x = 0
	for number in lst:
		while x < 1:
			limiteInferior = number
			x += 1
		limiteSuperior = limiteInferior + IC - 1
		listaIntervalos.append((limiteInferior, limiteSuperior))
		limiteInferior = limiteSuperior + 1
		if limiteSuperior >= valorMayor: 
			break
	return listaIntervalos
	
def marca_de_clase(listaIntervalos): #Crea una lista y almacena las marcas de clase de la distribucion
	global marcaDeClase
	marcaDeClase = []
	for x, y in listaIntervalos:
		z = x + y
		z = z / 2.0
		marcaDeClase.append(z)
	return marcaDeClase
	
def frecuencia_absoluta(lst): # Crea dos listas, una con la frecuencia absoluta simple y  otra con la acumulada.
	global frecuenciaS
	global frecuenciaSAcum
	frecuenciaS = []
	posicion = 0
	cuentaSimple = 0
	frecuenciaSAcum = []
	for x, y in listaIntervalos:
		for number in range(x, (y+1)):
			if number in lst:
				value = lst.count(number)
				cuentaSimple = value + cuentaSimple
		frecuenciaS.append(cuentaSimple)
		cuentaSimple = 0
	for numbers in frecuenciaS:
		try:
			frecuenciaSAcum.append(frecuenciaSAcum[posicion] + frecuenciaS[posicion + 1])
			posicion += 1
		except:
			frecuenciaSAcum.append(frecuenciaS[posicion]) 
	return frecuenciaS and frecuenciaSAcum
	
def frecuencia_relativa(frecuenciaS): #Crea cuatro listas, una de la frecuencia relativa, otra la relativa acumulada, otra con la frecuencia relativa porcentual y luego porcentual acumulada
	global frecuenciaR
	global frecuenciaRAcum
	global frecuencia100
	global frecuencia100Acum
	frecuenciaR = []
	frecuenciaRAcum = []
	frecuencia100 = []
	frecuencia100Acum = []
	sumatoriaRelativa = 0
	posicion = 0
	for i in frecuenciaS:
		frecuenciaR.append(i / float(len(lst)))
	for number in frecuenciaR:
		sumatoriaRelativa += number
	for j in frecuenciaR:
		try:
			frecuenciaRAcum.append(frecuenciaRAcum[posicion] + frecuenciaR[posicion + 1])
			posicion += 1
		except:
			frecuenciaRAcum.append(frecuenciaR[posicion])
	posicion = 0
	for e in frecuenciaR:
		frecuencia100.append(frecuenciaR[posicion] * 100)
		posicion += 1
	posicion = 0
	for every_number in frecuencia100:
		try:
			frecuencia100Acum.append(frecuencia100[posicion + 1] + frecuencia100Acum[posicion])
			posicion += 1
		except:
			frecuencia100Acum.append(frecuencia100[posicion])
	return frecuenciaR and frecuenciaRAcum and frecuencia100 and frecuencia100Acum
			
def media_geometrica(marcaDeClase): #Calcula la media geometrica de la distribucion
	sumatoriaGeometria = 0
	posicion = 0
	mediaGeometric = 0
	moda = None
	for marca in marcaDeClase:
		sumatoriaGeometria += (math.log10(marca) * frecuenciaS[posicion])
		posicion += 1
	mediaGeometric = round(10 ** round((sumatoriaGeometria / float(len(lst))), 4), 2)
	for current_number in frecuenciaS:
		if moda < current_number or moda == None:
			moda = current_number
	print "La media geometrica es:", mediaGeometric
	print "La moda es: ", moda
	return mediaGeometric
def medianaF(frecuenciaSAcum, frecuenciaS): # Calcula la mediana de la distribucion
	posicion = 0
	global mediana
	global temp
	temp = len(lst) / 2.0
	limiteInferior = 0
	for number in frecuenciaSAcum:
		if temp <= number:
			tuptemp = listaIntervalos[posicion]
			limiteInferior = tuptemp[0]
			break
		else:
			posicion += 1
	try:
		mediana = limiteInferior + ((((len(lst) / 2) - frecuenciaSAcum[posicion - 1]) / float(frecuenciaS[posicion])) * IC)
	except:
		mediana = limiteInferior + ((((len(lst) / 2) - 0) / float(frecuenciaS[posicion])) * IC)
	print "La mediana es: ",round(mediana, 2)

def medidas_de_posicion(listaIntervalos, frecuenciaS): #Calcula los percentiles, cuartiles, deciles y sextiles que el usuario desee.
	salida = ""
	linea = ""
	respuestaBool = raw_input("Desea calcular alguna medida de posicion? Si/No: ")
	while respuestaBool == "Si":
		print "Que medida de posicion desea calcular? \n1. Cuartil.\n2. Decil.\n3. Percentil.\n4. Sextil. \n5. Cancelar"
		try:
			n = int(raw_input("\nIntroduzca el numero de la medida de posicion que desea calcular: "))
			if n == 1:
				n = 4
				A = raw_input("Introduzca el cuartil que desea calcular: ")
				try:
					A = int(A)
					if A >= 1 and A <= 3:
						A = str(A)
						linea = "El cuartil "+ A 
						A = int(A)
					else:
						print "Por favor introduzca un valor entre 1 y 3"
						continue
				except:
					print "Por favor introduzca un valor numerico entre 1 y 3."
					continue
			elif n == 2:
				n = 10
				A = raw_input("Introduzca el decil que desea calcular: ")
				try:
					A = int(A)
					if A >= 1 and A <= 10:
						A = str(A)
						linea = "El decil "+ A
						A = int(A)
					else:
						print "Por favor introduzca un valor entre 1 y 10"
						continue
				except:
					print "Por favor introduzca un valor numerico entre 1 y 10"
					continue
			elif n == 3:
				n = 100
				A = raw_input("Introduzca el percentil que desea calcular: ")
				try:
					A = int(A)
					if A >= 1 and A <= 100:
						A = str(A)
						linea = "El percentil "+ A
						A = int(A)
					else:
						print "Por favor introduzca un valor entre 1 y 100"
						continue
				except:
					print "Por favor introduzca un valor numerico entre 1 y 100"
					continue
			elif n == 4:
				n = 6
				A = raw_input("Introduzca el sextil que desea calcular: ")
				try:
					A = int(A)
					if A >= 1 and A <= 6:
						A = str(A)
						linea = "El sextil "+ A 
						A = int(A)
					else:
						print "Por favor introduzca un valor entre 1 y 6"
						continue
				except:
					print "Por favor introduzca un valor numerico entre 1 y 6"
			elif n == 5:
				break
			else:
				print "Por favor seleccione una de las opciones"
				continue
		except:
			print "Por favor ingrese un valor numerico."
			continue
		posicion = 0
		posicionQ = (A * len(lst)) / float(n)
		for limiteInferior, limiteSuperior in listaIntervalos:
			if posicionQ <= frecuenciaSAcum[posicion]:
				if (posicion - 1) >= 0:
					Q = limiteInferior + (((posicionQ - frecuenciaSAcum[posicion - 1])/ float(frecuenciaS[posicion]))* IC)
					break
					posicion += 1
				else:
					Q = limiteInferior + ((posicionQ / float(frecuenciaS[posicion]))* IC)
					break
			else:
				posicion += 1
		Q = round(Q)
		linea = linea + " es: " + str(Q) +  "\n"
		salida += linea
		respuestaBool = raw_input("Desea calcular algo mas? Si/No: ")
	print salida
def medidas_de_dispersion(marcaDeClase, frecuenciaS): #Calcula las medidas de dispersion
	posicion = 0
	A = 1
	while A < 4:
		if A == 2:
			A += 1
			continue
		else:
			posicionQ = (A * len(lst)) / float(4)
			for limiteInferior, limiteSuperior in listaIntervalos:
				if posicionQ <= frecuenciaSAcum[posicion]:
					if (posicion - 1) >= 0:
						if A == 3:
							Q3 = limiteInferior + (((posicionQ - frecuenciaSAcum[posicion - 1])/ float(frecuenciaS[posicion]))* IC)
							break
						if A == 1:
							Q1 = limiteInferior + (((posicionQ - frecuenciaSAcum[posicion - 1])/ float(frecuenciaS[posicion]))* IC)
							break
					else:
						if A == 3:
							Q3 = limiteInferior + ((posicionQ / float(frecuenciaS[posicion]))* IC)
							break
						if A == 1:
							Q1 = limiteInferior + ((posicionQ / float(frecuenciaS[posicion]))* IC)
							break
				else:
					posicion += 1
			A += 1
			posicion = 0
	Q3 = round(Q3)
	Q1 = round(Q1)
	desviacion_cuartilica = Q3 - Q1
	desviacion_intercuartil = (Q3 - Q1) / 2.0
	posicion = 0
	sumatoria_desviacion = 0
	for every_clase in marcaDeClase:
		sumatoria_desviacion += (abs(every_clase - mediaPoblacional) * frecuenciaS[posicion])		
		posicion += 1
	desviacion_media = sumatoria_desviacion / float(len(lst))
	sumatoria_varianza = 0
	posicion = 0
	for every_clase in marcaDeClase:
		sumatoria_varianza += ((abs(every_clase - mediaPoblacional)**2) * frecuenciaS[posicion])
		posicion += 1
	desviacion_media = round(desviacion_media,3)
	varianza = sumatoria_varianza / (float(len(lst)))
	try:
		desviacion_tipica = math.sqrt(varianza)
		desviacion_tipica = round(desviacion_tipica, 3)
		coeficiente_de_variacion = (desviacion_tipica / float(mediaPoblacional)) * 100 
		coeficiente_de_variacion = round(coeficiente_de_variacion, 3)
		coeficiente_de_pearson = (3 * (mediaPoblacional - round(mediana))) / float(desviacion_tipica)
		coeficiente_de_bowley = (Q3 + Q1 - (2 * round(mediana))) / float(Q3 - Q1)
		posicion = 0
		sumatoriaM4 = 0
		for marca in marcaDeClase:
			sumatoriaM4 += (abs(marca - mediaPoblacional) ** 4) * frecuenciaS[posicion]
			posicion += 1
		M4 = sumatoriaM4 / float(len(lst))
		M4 = round(M4)
		K = M4 / float(round((varianza)**2))
		K = round(K,2)
		print "La desviacion cuartilica es: ",desviacion_cuartilica
		print "La desviacion intercuartilica es: ",desviacion_intercuartil
		print "La desviacion media es: ",desviacion_media
		print "La varianza es: ",round(varianza,3)
		print "La desviacion tipica es: ",desviacion_tipica
		print "El coeficiente de variacion es: ",coeficiente_de_variacion
		print "El coeficiente de pearson es: ",round(coeficiente_de_pearson,2)
		print "El coeficiente de bowley es: ",round(coeficiente_de_bowley,2)
		if K < 3:
			print "La curtosis es "+ str(K) +" y es platicurtica."
		elif K == 3:
			print "La curtosis es "+ str(K) +" y es mesocurtica."
		elif K > 3:
			print "La curtosis es "+ str(K) +" y es leptocurtica."		
	except:
		print "No se puede calcular el coeficiente de pearson."
		print "No se puede calcular el coeficiente de bowley."
		print "La varianza es cero."
		print "El coeficiente de variacion es cero."
		print "La desviacion tipica es cero."
		print "No se puede calcular la curtosis."

	
def media_poblacional(product): #Calcula la media poblacional y la imprime
	global mediaPoblacional
	mediaPoblacional = product / float(len(lst))
	print "La media aritmetica es:", round(mediaPoblacional, 2)
	return mediaPoblacional
def imprime_tabla(listaIntervalos): #Imprime la tabla de frecuencias 
	fila = []
	posicion = 0
	for x, y in listaIntervalos:
		valores = []
		valores.append((x,y))
		valores.append(marcaDeClase[posicion])
		valores.append(frecuenciaS[posicion])
		valores.append(frecuenciaSAcum[posicion])
		valores.append("{:10.4f}".format(frecuenciaR[posicion]))
		valores.append("{:10.4f}".format(frecuenciaRAcum[posicion]))
		valores.append("{:10.4f}".format(frecuencia100[posicion]))
		valores.append("{:10.4f}".format(frecuencia100Acum[posicion]))
		fila.append(valores)
		posicion += 1
	print tabulate(fila, ["IC", "Xi", "fi", "Fi", "hi", "Hi", "hi * 100", "Hi * 100"], tablefmt="grid")
obtiene_numeros()
suma_numeros()
media_poblacional(product)
pow_numbers()
atr_ic()
intervalos_de_clase(IC, lst)
marca_de_clase(listaIntervalos)
frecuencia_absoluta(lst)
frecuencia_relativa(frecuenciaS)
imprime_tabla(listaIntervalos)
media_geometrica(marcaDeClase)
medianaF(frecuenciaSAcum, frecuenciaS)
medidas_de_dispersion(marcaDeClase, frecuenciaS)
medidas_de_posicion(listaIntervalos, frecuenciaS)
