import math
from tabulate import tabulate


class Statistics:
    def __init__(self):
        self.lst = []
        self.product = 0
        self.intervals = []
        self.highestValue = None
        self.classMarks = []
        self.intervalsList = []
        self.relativeFrequency = []
        self.absFrequencyCumulative = []
        self.relativeFrequencyAcum = []
        self.porcentualRelFrequency = []
        self.porcentualRelFrequencyAcum = []
        self.simpleAbsFrequency = []
        self.absFrequencyCumulative = []

    def asks_numbers(self): 
        """
            Asks for every number in the data distribution
        """
        count = 0
        try:
            quantityData = int(raw_input("Input the quantity of data in the distribution: "))
        except:
            print "Please input a numeric value."
        while count < quantityData:
            try:
                number = int(raw_input("Input data: "))
                self.lst.append(number)
                count += 1
            except:
                print "Please input a numeric value."
        self.lst.sort()
        return self.lst

    def sum_numbers(self):
        """
            Calculates the sum of the numbers
        """
        self.product = 0
        for value in self.lst:
            self.product += value

    def pow_numbers(self): 
        """
            Calculates the sum of the quadratic power of every value
        """
        temp = 0
        for i in self.lst:
            temp += (i - self.arithmeticMean) ** 2

    def class_amplitude(self):
        """
            Calculates the class intervals.
        """
        self.highestValue = max(self.lst)
        smallestValue = min(self.lst)
        ATR = self.highestValue - smallestValue + 1
        self.intervals = ATR / round((1 + 3.322 * math.log10(len(self.lst))))
        self.intervals = int(round(self.intervals))

    def class_intervals(self):
        """
            Generates the class intervals and puts them in a list.
        """
        x = 0
        for number in self.lst:  # Goes through every value and asigns the upper and lower limits for every class
            while x < 1:  # Asigns the first lowerLimit
                lowerLimit = number
                x += 1
            upperLimit = lowerLimit + self.intervals - 1  # Asigns the upperLimit
            self.intervalsList.append((lowerLimit, upperLimit))  # Adds a tuple to the list that represents the class
            lowerLimit = upperLimit + 1  # Asigns the following lowerLimit
            if upperLimit >= self.highestValue:  # Stops the loop once it reached or went over the highestValue
                break

    def class_marks(self):
        """
            Creates a list and stores the class marks for every class interval.
        """
        for x, y in self.intervalsList:
            z = (x + y) / 2.0
            self.classMarks.append(z)

    def absolute_frequency(self):
        """
            Creates two lists, one with the calculated simple absolute frequency and other with its cumulative value
        """
        position = 0
        simpleCount = 0
        for x, y in self.intervalsList:  # Goes through every class interval
            for number in range(x, (y + 1)):  # Goes through every number in the range of the current interval
                if number in self.lst:  # Checks to see if the number is in the distribution and then counts how many times.
                    value = self.lst.count(number)
                    simpleCount += value
            self.simpleAbsFrequency.append(simpleCount)
            simpleCount = 0
        for numbers in self.simpleAbsFrequency:  # Goes through every frequency and adds it up to the cumulative list.
            try:
                self.absFrequencyCumulative.append(
                    self.absFrequencyCumulative[position] + self.simpleAbsFrequency[position + 1])
                position += 1
            except:
                self.absFrequencyCumulative.append(self.simpleAbsFrequency[position])
        print self.intervalsList, self.simpleAbsFrequency

    def relative_frequency(self):
        """
            Calculates the relative frequency, the cumulative relative frequency and the porcentual form.
        """
        relativeSum = 0
        position = 0
        for i in self.simpleAbsFrequency:
            self.relativeFrequency.append(i / float(len(self.lst)))
        for number in self.relativeFrequency:
            relativeSum += number
        for j in self.relativeFrequency:
            try:
                self.relativeFrequencyAcum.append(
                    self.relativeFrequencyAcum[position] + self.relativeFrequency[position + 1])
                position += 1
            except:
                self.relativeFrequencyAcum.append(self.relativeFrequency[position])
        position = 0
        for e in self.relativeFrequency:
            self.porcentualRelFrequency.append(self.relativeFrequency[position] * 100)
            position += 1
        position = 0
        for every_number in self.porcentualRelFrequency:
            try:
                self.porcentualRelFrequencyAcum.append(
                    self.porcentualRelFrequency[position + 1] + self.porcentualRelFrequencyAcum[position])
                position += 1
            except:
                self.porcentualRelFrequencyAcum.append(self.porcentualRelFrequency[position])

    def geometric_mean(self): 
        """
            Calcutes the geometric mean and the mode.
        """
        geometricSum = 0
        position = 0
        geometricMean = 0
        mode = None
        for mark in self.classMarks:
            geometricSum += (math.log10(mark) * self.simpleAbsFrequency[position])
            position += 1
        geometricMean = round(10 ** round((geometricSum / float(len(self.lst))), 4), 2)
        for current_number in self.simpleAbsFrequency:
            if mode < current_number or mode is None:
                mode = current_number
        print "The geometric mean is:", geometricMean
        print "The mode is: ", mode

    def median(self):
        """
            Calculates the median of the distribution
        """
        position = 0
        temp = len(self.lst) / 2.0
        lowerLimit = 0
        for number in self.absFrequencyCumulative:
            if temp <= number:
                tuptemp = self.intervalsList[position]
                lowerLimit = tuptemp[0]
                break
            else:
                position += 1
        try:
            self.medianD = lowerLimit + ((((len(self.lst) / 2) - self.absFrequencyCumulative[position - 1]) / float(
                self.simpleAbsFrequency[position])) * self.intervals)
        except:
            self.medianD = lowerLimit + ((((len(self.lst) / 2) - 0) / float(self.simpleAbsFrequency[position])) * self.intervals)
        print "La median is ", round(self.medianD, 2)

    def measure_of_position(self):
        """
            Calculates the measures of position
        """
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
                            line = "The quartile " + A
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
                            line = "The decile " + A
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
                            line = "The percentile " + A
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
                            line = "The sextile " + A
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
            positionQ = (A * len(self.lst)) / float(n)
            for lowerLimit, upperLimit in self.intervalsList:
                if positionQ <= self.absFrequencyCumulative[position]:
                    if (position - 1) >= 0:
                        Q = lowerLimit + (((positionQ - self.absFrequencyCumulative[position - 1]) / float(
                            self.simpleAbsFrequency[position])) * self.intervals)
                        break
                        position += 1
                    else:
                        Q = lowerLimit + ((positionQ / float(self.simpleAbsFrequency[position])) * self.intervals)
                        break
                else:
                    position += 1
            Q = round(Q)
            line = line + " is: " + str(Q) + "\n"
            output += line
            respuestaBool = raw_input("Do you want to calculate anything else? Yes/No: ")
        print output

    def measures_of_dispersion(self):
        """
            Calculates the measures of dispersion
        """
        position = 0
        A = 1
        while A < 4:
            if A == 2:
                A += 1
                continue
            else:
                positionQ = (A * len(self.lst)) / float(4)
                for lowerLimit, upperLimit in self.intervalsList:
                    if positionQ <= self.absFrequencyCumulative[position]:
                        if (position - 1) >= 0:
                            if A == 3:
                                q3 = lowerLimit + (((positionQ - self.absFrequencyCumulative[position - 1]) / float(
                                    self.simpleAbsFrequency[position])) * self.intervals)
                                break
                            if A == 1:
                                q1 = lowerLimit + (((positionQ - self.absFrequencyCumulative[position - 1]) / float(
                                    self.simpleAbsFrequency[position])) * self.intervals)
                                break
                        else:
                            if A == 3:
                                q3 = lowerLimit + (
                                (positionQ / float(self.simpleAbsFrequency[position])) * self.intervals)
                                break
                            if A == 1:
                                q1 = lowerLimit + (
                                (positionQ / float(self.simpleAbsFrequency[position])) * self.intervals)
                                break
                    else:
                        position += 1
                A += 1
                position = 0
        q3 = round(q3)
        q1 = round(q1)
        quartileDeviation = q3 - q1
        interquartileDeviation = (q3 - q1) / 2.0
        position = 0
        deviationSum = 0
        for every_class in self.classMarks:
            deviationSum += (abs(every_class - self.arithmeticMean) * self.simpleAbsFrequency[position])
            position += 1
        meanDeviation = deviationSum / float(len(self.lst))
        varianceSum = 0
        position = 0
        for every_class in self.classMarks:
            varianceSum += ((abs(every_class - self.arithmeticMean) ** 2) * self.simpleAbsFrequency[position])
            position += 1
        meanDeviation = round(meanDeviation, 3)
        variance = varianceSum / (float(len(self.lst)))
        if variance != 0:
            standardDeviation = math.sqrt(variance)
            standardDeviation = round(standardDeviation, 3)
            varianceCoefficient = (standardDeviation / float(self.arithmeticMean)) * 100
            varianceCoefficient = round(varianceCoefficient, 3)
            pearsonCoefficient = (3 * (self.arithmeticMean - round(self.medianD))) / float(standardDeviation)
            bowleyCoefficient = (q3 + q1 - (2 * round(self.medianD))) / float(q3 - q1)
            position = 0
            m4Sum = 0
            for marca in self.classMarks:
                m4Sum += (abs(marca - self.arithmeticMean) ** 4) * self.simpleAbsFrequency[position]
                position += 1
            M4 = m4Sum / float(len(self.lst))
            M4 = round(M4)
            K = M4 / float(round((variance) ** 2))
            K = round(K, 2)
            print "The quartile deviation is ", quartileDeviation
            print "The interquartile deviation  is ", interquartileDeviation
            print "The mean deviation is ", meanDeviation
            print "The variance is ", round(variance, 3)
            print "The standard deviation is ", standardDeviation
            print "The variance coefficient is ", varianceCoefficient
            print "The pearson coefficient is ", round(pearsonCoefficient, 2)
            print "The bowley coefficient is ", round(bowleyCoefficient, 2)
            if K < 3:
                print "The kurtosis is " + str(K) + " and is platykurtic."
            elif K == 3:
                print "The kurtosis is " + str(K) + " and is mesokurtic."
            elif K > 3:
                print "The kurtosis is " + str(K) + " and is leptokurtic."
        else:
            print "The bowley coefficient can't be calculated."
            print "The pearson coefficient can't be calculated."
            print "The variance is zero."
            print "The variance coefficient is zero."
            print "The standard deviation is zero."
            print "The kurtosis can't be calculated."

    def arithmetic_mean(self):  # Calculates the arithmetic mean and prints it
        self.arithmeticMean = self.product / float(len(self.lst))
        print "The arithmetic mean is ", round(self.arithmeticMean, 2)

    def print_table(self):  # Imprime la tabla de simpleAbsFrequency
        row = []
        position = 0
        for x, y in self.intervalsList:
            values = []
            values.append((x, y))
            values.append(self.classMarks[position])
            values.append(self.simpleAbsFrequency[position])
            values.append(self.absFrequencyCumulative[position])
            values.append("{:10.4f}".format(self.relativeFrequency[position]))
            values.append("{:10.4f}".format(self.relativeFrequencyAcum[position]))
            values.append("{:10.4f}".format(self.porcentualRelFrequency[position]))
            values.append("{:10.4f}".format(self.porcentualRelFrequencyAcum[position]))
            row.append(values)
            position += 1
        print tabulate(row, ["IC", "Xi", "fi", "Fi", "hi", "Hi", "hi * 100", "Hi * 100"], tablefmt="grid")


object = Statistics()
object.asks_numbers()
object.sum_numbers()
object.arithmetic_mean()
object.pow_numbers()
object.class_amplitude()
object.class_intervals()
object.class_marks()
object.absolute_frequency()
object.relative_frequency()
object.print_table()
object.geometric_mean()
object.median()
object.measures_of_dispersion()
object.measure_of_position()
