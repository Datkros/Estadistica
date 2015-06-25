import math
from tabulate import tabulate

def asks_numbers(): # Asks for every value in the data distribution
	global lst
	lst = []
	count = 0
	try:
		cantidad_datos = int(raw_input("Input the quantity of data in the distribution: "))
		while count < cantidad_datos:
			try:
				number = int(raw_input("Input data: "))
				lst.append(number)
				count += 1
			except:
				print "Please input a numeric value."
		lst.sort()
	except:
		print "Please input a numeric value."
	return lst
		

def sum_numbers(): #Calculates the sum of the numbers
	global product
	product = 0
	for Value in lst: 
		product += Value
	return product

def pow_numbers(): #Calculates the sum of the quadratic power of every value 
	temp = 0
	for i in lst:
		temp += (i - arithmeticMean)**2

def atr_ic(): # Calculates the class intervals.
	global IC
	global highestValue
	highestValue = max(lst)
	smallestValue = min(lst)
	ATR = highestValue - smallestValue + 1
	IC = ATR / round((1 + 3.322 * math.log10(len(lst))))
	IC = int(round(IC))

def class_intervals(IC, lst): # Generates the class intervals and puts them in a list.
	global intervalsList
	intervalsList = []
	x = 0
	for number in lst: #Goes through every value and asigns the upper and lower limits for every class
		while x < 1: # Asigns the first lowerLimit
			lowerLimit = number
			x += 1
		upperLimit = lowerLimit + IC - 1 #Asigns the lowerLimit
		intervalsList.append((lowerLimit, upperLimit)) #Adds a tuple to the list that represents the class
		lowerLimit = upperLimit + 1 #Asigns the following lowerLimit
		if upperLimit >= highestValue:  #Stops the loop once it reached or went over the highestValue
			break
	return intervalsList
	
def class_marks(intervalsList): #Creates a list and stores the class marks for every class interval. 
	global classMarks
	classMarks = []
	for x, y in intervalsList:
		z = x + y
		z = z / 2.0
		classMarks.append(z)
	return classMarks
	
def absolute_frequency(lst): # Creates two lists, one with the calculated simple absolute frequency and other with its cumulative value
	global simpleAbsFrequency
	global absFrequencyCumulative
	simpleAbsFrequency = []
	position = 0
	simpleCount = 0
	absFrequencyCumulative = []
	for x, y in intervalsList: #Goes through every class interval 
		for number in range(x, (y+1)): #Goes through every number in the range of the current interval
			if number in lst: # Checks to see if the number is in the distribution and then counts how many times.
				value = lst.count(number)
				simpleCount = value + simpleCount
		simpleAbsFrequency.append(simpleCount)
		simpleCount = 0
	for numbers in simpleAbsFrequency: #Goes through every frequency and adds it up to the cumulative list. 
		try:
			absFrequencyCumulative.append(absFrequencyCumulative[position] + simpleAbsFrequency[position + 1])
			position += 1
		except:
			absFrequencyCumulative.append(simpleAbsFrequency[position]) 
	return simpleAbsFrequency and absFrequencyCumulative
	
def relative_frequency(simpleAbsFrequency): #Calculates the relative frequency, the cumulative relative frequency and the porcentual form.
	global relative_frequency
	global relative_frequencyAcum
	global porcentualRelFrequency
	global porcentualRelFrequencyAcum
	relative_frequency = []
	relative_frequencyAcum = []
	porcentualRelFrequency = []
	porcentualRelFrequencyAcum = []
	relativeSum = 0
	position = 0
	for i in simpleAbsFrequency:
		relative_frequency.append(i / float(len(lst)))
	for number in relative_frequency:
		relativeSum += number
	for j in relative_frequency:
		try:
			relative_frequencyAcum.append(relative_frequencyAcum[position] + relative_frequency[position + 1])
			position += 1
		except:
			relative_frequencyAcum.append(relative_frequency[position])
	position = 0
	for e in relative_frequency:
		porcentualRelFrequency.append(relative_frequency[position] * 100)
		position += 1
	position = 0
	for every_number in porcentualRelFrequency:
		try:
			porcentualRelFrequencyAcum.append(porcentualRelFrequency[position + 1] + porcentualRelFrequencyAcum[position])
			position += 1
		except:
			porcentualRelFrequencyAcum.append(porcentualRelFrequency[position])
	return relative_frequency and relative_frequencyAcum and porcentualRelFrequency and porcentualRelFrequencyAcum
			
def geometric_mean(classMarks): #Calcutes the geometric mean and the mode.
	geometricSum = 0
	position = 0
	geometricMean = 0
	mode = None
	for mark in classMarks:
		geometricSum += (math.log10(mark) * simpleAbsFrequency[position])
		position += 1
	geometricMean = round(10 ** round((geometricSum / float(len(lst))), 4), 2)
	for current_number in simpleAbsFrequency:
		if mode < current_number or mode == None:
			mode = current_number
	print "The geometric mean is:", geometricMean
	print "The mode is: ", mode
	return geometricMean
def median(absFrequencyCumulative, simpleAbsFrequency): # Calculates the median of the distribution
	position = 0
	global medianD
	global temp
	temp = len(lst) / 2.0
	lowerLimit = 0
	for number in absFrequencyCumulative:
		if temp <= number:
			tuptemp = intervalsList[position]
			lowerLimit = tuptemp[0]
			break
		else:
			position += 1
	try:
		medianD = lowerLimit + ((((len(lst) / 2) - absFrequencyCumulative[position - 1]) / float(simpleAbsFrequency[position])) * IC)
	except:
		medianD = lowerLimit + ((((len(lst) / 2) - 0) / float(simpleAbsFrequency[position])) * IC)
	print "La median is ",round(medianD, 2)

def measure_of_position(intervalsList, simpleAbsFrequency): #Calculates the measures of position
	output = ""
	line = ""
	respuestaBool = raw_input("Do you want to calculate any measure of position? Yes/No: ")
	while respuestaBool == "Yes" or respuestaBool == "yes":
		print "What measure of position do you want to calculate? \n1. Quartile.\n2. Decile.\n3. Percentile.\n4. Sextile. \n5. Cancel"
		try:
			n = int(raw_input("\nInput the number of the measure of position you want to calculate: "))
			if n == 1:
				n = 4
				A = raw_input("Input the number of the quartile you want to calculate: ")
				try:
					A = int(A)
					if A >= 1 and A <= 3:
						A = str(A)
						line = "The quartile "+ A 
						A = int(A)
					else:
						print "Please input a value between 1 y 3"
						continue
				except:
					print "Please input a numeric value between 1 y 3."
					continue
			elif n == 2:
				n = 10
				A = raw_input("Input the number of the decile you want to calculate: ")
				try:
					A = int(A)
					if A >= 1 and A <= 10:
						A = str(A)
						line = "The decile "+ A
						A = int(A)
					else:
						print "Please input a value between 1 y 10"
						continue
				except:
					print "Please input a value between 1 y 10"
					continue
			elif n == 3:
				n = 100
				A = raw_input("Input the number of the percentile you want to calculate: ")
				try:
					A = int(A)
					if A >= 1 and A <= 100:
						A = str(A)
						line = "The percentile "+ A
						A = int(A)
					else:
						print "Please input a value between 1 y 100"
						continue
				except:
					print "Please input a numeric value between 1 y 100"
					continue
			elif n == 4:
				n = 6
				A = raw_input("Input the sextile you want to calculate: ")
				try:
					A = int(A)
					if A >= 1 and A <= 6:
						A = str(A)
						line = "The sextile "+ A 
						A = int(A)
					else:
						print "Please input a value between 1 y 6"
						continue
				except:
					print "Please input a numeric value between 1 y 6"
			elif n == 5:
				break
			else:
				print "Please select one of the options."
				continue
		except:
			print "Please input a numeric value."
			continue
		position = 0
		positionQ = (A * len(lst)) / float(n)
		for lowerLimit, upperLimit in intervalsList:
			if positionQ <= absFrequencyCumulative[position]:
				if (position - 1) >= 0:
					Q = lowerLimit + (((positionQ - absFrequencyCumulative[position - 1])/ float(simpleAbsFrequency[position]))* IC)
					break
					position += 1
				else:
					Q = lowerLimit + ((positionQ / float(simpleAbsFrequency[position]))* IC)
					break
			else:
				position += 1
		Q = round(Q)
		line = line + " is: " + str(Q) +  "\n"
		output += line
		respuestaBool = raw_input("Do you want to calculate anything else? Yes/No: ")
	print output
def measures_of_dispersion(classMarks, simpleAbsFrequency): #Calculates the measures of dispersion
	position = 0
	A = 1
	while A < 4:
		if A == 2:
			A += 1
			continue
		else:
			positionQ = (A * len(lst)) / float(4)
			for lowerLimit, upperLimit in intervalsList:
				if positionQ <= absFrequencyCumulative[position]:
					if (position - 1) >= 0:
						if A == 3:
							Q3 = lowerLimit + (((positionQ - absFrequencyCumulative[position - 1])/ float(simpleAbsFrequency[position]))* IC)
							break
						if A == 1:
							Q1 = lowerLimit + (((positionQ - absFrequencyCumulative[position - 1])/ float(simpleAbsFrequency[position]))* IC)
							break
					else:
						if A == 3:
							Q3 = lowerLimit + ((positionQ / float(simpleAbsFrequency[position]))* IC)
							break
						if A == 1:
							Q1 = lowerLimit + ((positionQ / float(simpleAbsFrequency[position]))* IC)
							break
				else:
					position += 1
			A += 1
			position = 0
	Q3 = round(Q3)
	Q1 = round(Q1)
	quartileDeviation = Q3 - Q1
	interquartileDeviation = (Q3 - Q1) / 2.0
	position = 0
	deviationSum = 0
	for every_class in classMarks:
		deviationSum += (abs(every_class - arithmeticMean) * simpleAbsFrequency[position])		
		position += 1
	meanDeviation = deviationSum / float(len(lst))
	varianceSum = 0
	position = 0
	for every_class in classMarks:
		varianceSum += ((abs(every_class - arithmeticMean)**2) * simpleAbsFrequency[position])
		position += 1
	meanDeviation = round(meanDeviation,3)
	variance = varianceSum / (float(len(lst)))
	try:
		standardDeviation = math.sqrt(variance)
		standardDeviation = round(standardDeviation, 3)
		varianceCoefficient = (standardDeviation / float(arithmeticMean)) * 100 
		varianceCoefficient = round(varianceCoefficient, 3)
		pearsonCoefficient = (3 * (arithmeticMean - round(medianD))) / float(standardDeviation)
		bowleyCoefficient = (Q3 + Q1 - (2 * round(medianD))) / float(Q3 - Q1)
		position = 0
		m4Sum = 0
		for marca in classMarks:
			m4Sum += (abs(marca - arithmeticMean) ** 4) * simpleAbsFrequency[position]
			position += 1
		M4 = m4Sum / float(len(lst))
		M4 = round(M4)
		K = M4 / float(round((variance)**2))
		K = round(K,2)
		print "The quartile deviation is ",quartileDeviation
		print "The interquartile deviation  is ",interquartileDeviation
		print "The mean deviation is ",meanDeviation
		print "The variance is ",round(variance,3)
		print "The standard deviation is ",standardDeviation
		print "The variance coefficient is ",varianceCoefficient
		print "The pearson coefficient is ",round(pearsonCoefficient,2)
		print "The bowley coefficient is ",round(bowleyCoefficient,2)
		if K < 3:
			print "The kurtosis is "+ str(K) +" and is platykurtic."
		elif K == 3:
			print "The kurtosis is "+ str(K) +" and is mesokurtic."
		elif K > 3:
			print "The kurtosis is "+ str(K) +" and is leptokurtic."		
	except:
		print "The bowley coefficient can't be calculated."
		print "The pearson coefficient can't be calculated."
		print "The variance is zero."
		print "The variance coefficient is zero."
		print "The standard deviation is zero."
		print "The kurtosis can't be calculated."

	
def arithmetic_mean(product): #Calculates the arithmetic mean and prints it
	global arithmeticMean
	arithmeticMean = product / float(len(lst))
	print "The arithmetic mean is ", round(arithmeticMean, 2)
	return arithmeticMean
def imprime_tabla(intervalsList): #Prints the frequency distribution table
	row = []
	position = 0
	for x, y in intervalsList:
		values = []
		values.append((x,y))
		values.append(classMarks[position])
		values.append(simpleAbsFrequency[position])
		values.append(absFrequencyCumulative[position])
		values.append("{:10.4f}".format(relative_frequency[position]))
		values.append("{:10.4f}".format(relative_frequencyAcum[position]))
		values.append("{:10.4f}".format(porcentualRelFrequency[position]))
		values.append("{:10.4f}".format(porcentualRelFrequencyAcum[position]))
		row.append(values)
		position += 1
	print tabulate(row, ["IC", "Xi", "fi", "Fi", "hi", "Hi", "hi * 100", "Hi * 100"], tablefmt="grid")
asks_numbers()
sum_numbers()
arithmetic_mean(product)
pow_numbers()
atr_ic()
class_intervals(IC, lst)
class_marks(intervalsList)
absolute_frequency(lst)
relative_frequency(simpleAbsFrequency)
imprime_tabla(intervalsList)
geometric_mean(classMarks)
median(absFrequencyCumulative, simpleAbsFrequency)
measures_of_dispersion(classMarks, simpleAbsFrequency)
measure_of_position(intervalsList, simpleAbsFrequency)
