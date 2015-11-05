__author__ = 'Victor'
from gooey import Gooey
import argparse
import math
from tabulate import tabulate


class Statistics:
    def __init__(self):
        lst = []
        self.product = 0
        self.intervals = 0
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
        self.q3 = 0
        self.q1 = 0
        self.variance = 0
        self.standardDeviation = 0

    def sum_numbers(self, lst):  # Calculates the sum of the numbers
        self.product = 0
        for value in lst:
            self.product += value

    def pow_numbers(self, lst):  # Calculates the sum of the quadratic power of every value
        temp = 0
        for i in lst:
            temp += (i - self.arithmeticMean) ** 2

    def class_amplitude(self, lst):  # Calculates the class intervals.
        self.highestValue = max(lst)
        smallestValue = min(lst)
        ATR = self.highestValue - smallestValue + 1
        self.intervals = ATR / round((1 + 3.322 * math.log10(len(lst))))
        self.intervals = int(round(self.intervals))

    def class_intervals(self, lst):  # Generates the class intervals and puts them in a list.
        x = 0
        for number in lst:  # Goes through every value and asigns the upper and lower limits for every class
            while x < 1:  # Asigns the first lowerLimit
                lowerLimit = number
                x += 1
            upperLimit = lowerLimit + self.intervals - 1  # Asigns the upperLimit
            self.intervalsList.append((lowerLimit, upperLimit))  # Adds a tuple to the list that represents the class
            lowerLimit = upperLimit + 1  # Asigns the following lowerLimit
            if upperLimit >= self.highestValue:  # Stops the loop once it reached or went over the highestValue
                break

    def class_marks(self):  # Creates a list and stores the class marks for every class interval.
        for x, y in self.intervalsList:
            z = (x + y) / 2.0
            self.classMarks.append(z)

    def absolute_frequency(self, lst):  # Creates two lists, one with the calculated simple absolute frequency and other with its cumulative value
        position = 0
        simpleCount = 0
        for x, y in self.intervalsList:  # Goes through every class interval
            for number in range(x, (y + 1)):  # Goes through every number in the range of the current interval
                if number in lst:  # Checks to see if the number is in the distribution and then counts how many times.
                    value = lst.count(number)
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

    def relative_frequency(self, lst):  # Calculates the relative frequency, the cumulative relative frequency and the porcentual form.
        relativeSum = 0
        position = 0
        for i in self.simpleAbsFrequency:
            self.relativeFrequency.append(i / float(len(lst)))
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

    def geometric_mean(self, lst):  # Calcutes the geometric mean and the mode.
        geometricSum = 0
        position = 0
        geometricMean = 0
        for mark in self.classMarks:
            geometricSum += (math.log10(mark) * self.simpleAbsFrequency[position])
            position += 1
        geometricMean = round(10 ** round((geometricSum / float(len(lst))), 4), 2)
        print "La media geometrica es: ", geometricMean

    def moda(self):
        mode = None
        for current_number in self.simpleAbsFrequency:
            if mode < current_number or mode is None:
                mode = current_number
        print "La moda es: ", mode

    def median(self, lst):  # Calculates the median of the distribution
        position = 0
        temp = len(lst) / 2.0
        lowerLimit = 0
        for number in self.absFrequencyCumulative:
            if temp <= number:
                tuptemp = self.intervalsList[position]
                lowerLimit = tuptemp[0]
                break
            else:
                position += 1
        try:
            self.medianD = lowerLimit + ((((len(lst) / 2) - self.absFrequencyCumulative[position - 1]) / float(
                self.simpleAbsFrequency[position])) * self.intervals)
        except:
            self.medianD = lowerLimit + ((((len(lst) / 2) - 0) / float(self.simpleAbsFrequency[position])) * self.intervals)
        print "La mediana es ", round(self.medianD, 2)

    def measure_of_position(self, lst, n, A):  # Calculates the measures of position
        position = 0
        positionQ = (A * len(lst)) / float(n)
        for lowerLimit, upperLimit in self.intervalsList:
            if positionQ <= self.absFrequencyCumulative[position]:
                if (position - 1) >= 0:
                    Q = lowerLimit + (((positionQ - self.absFrequencyCumulative[position - 1]) / float(
                    self.simpleAbsFrequency[position])) * self.intervals)
                    break
                else:
                    Q = lowerLimit + ((positionQ / float(self.simpleAbsFrequency[position])) * self.intervals)
                    break
            else:
                position += 1
        Q = round(Q)
        return Q

    def measures_of_dispersion(self, lst):  # Calculates the measures of dispersion
        position = 0
        A = 1
        while A < 4:
            if A == 2:
                A += 1
                continue
            else:
                positionQ = (A * len(lst)) / float(4)
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
        self.q3 = round(q3)
        self.q1 = round(q1)

    def quartile_deviation(self):
        quartileDeviation = self.q3 - self.q1
        print "La desviacion cuartilica es ", quartileDeviation

    def interquartile_deviation(self):
        interquartileDeviation = (self.q3 - self.q1) / 2.0
        print "La desviacion inter-cuartilica es ", interquartileDeviation

    def mean_deviation(self, lst):
        position = 0
        deviationSum = 0
        for every_class in self.classMarks:
            deviationSum += (abs(every_class - self.arithmeticMean) * self.simpleAbsFrequency[position])
            position += 1
        meanDeviation = deviationSum / float(len(lst))
        meanDeviation = round(meanDeviation, 3)
        print "La desviacion media es ", meanDeviation

    def variance_func(self, lst):
        varianceSum = 0
        position = 0
        for every_class in self.classMarks:
            varianceSum += ((abs(every_class - self.arithmeticMean) ** 2) * self.simpleAbsFrequency[position])
            position += 1
        self.variance = varianceSum / (float(len(lst)))
        print "La varianza es ", round(self.variance, 3)

    def standard_deviation(self, lst):
        if self.variance != 0:
            standardDeviation = math.sqrt(self.variance)
            self.standardDeviation = round(standardDeviation, 3)
            print "La desviacion estandar es ", self.standardDeviation
        else:
            print "La desviacion estandar es 0"

    def variance_coefficient(self):
        varianceCoefficient = (self.standardDeviation / float(self.arithmeticMean)) * 100
        varianceCoefficient = round(varianceCoefficient, 3)
        print "El coeficiente de viaracion es ", varianceCoefficient

    def pearson_coefficient(self):
        pearsonCoefficient = (3 * (self.arithmeticMean - round(self.medianD))) / float(self.standardDeviation)
        print "El coeficiente de Pearson es ", round(pearsonCoefficient, 2)

    def bowley_coefficient(self):
        bowleyCoefficient = (self.q3 + self.q1 - (2 * round(self.medianD))) / float(self.q3 - self.q1)
        print "El coeficiente de Bowley es ", round(bowleyCoefficient, 2)

    def kurtosis(self, lst):
        position = 0
        m4Sum = 0
        for marca in self.classMarks:
            m4Sum += (abs(marca - self.arithmeticMean) ** 4) * self.simpleAbsFrequency[position]
            position += 1
        M4 = m4Sum / float(len(lst))
        M4 = round(M4)
        K = M4 / float(round((self.variance) ** 2))
        K = round(K, 2)
        if K < 3:
            print "La curtosis es " + str(K) + " y es platicurtica."
        elif K == 3:
            print "La curtosis es " + str(K) + " y es mesocurtica."
        elif K > 3:
            print "La curtosis es " + str(K) + " y es leptocurtica."

    def arithmetic_mean(self, lst):  # Calculates the arithmetic mean and prints it
        self.arithmeticMean = self.product / float(len(lst))
        return round(self.arithmeticMean, 2)

    def print_table(self):  # Prints table
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
            values.append(self.classMarks[position] * self.simpleAbsFrequency[position])
            values.append(math.log10(self.classMarks[position] * self.simpleAbsFrequency[position]))
            row.append(values)
            position += 1
        print tabulate(row, ["IC", "Xi", "fi", "Fi", "hi", "Hi", "hi * 100", "Hi * 100", "Xi * fi", "log(Xi * fi)"], tablefmt="grid")
@Gooey(advanced=True, # toggle whether to show advanced config or not
       monospace_display = True,
       language='english',  # Translations configurable via json
       show_config=True,          # skip config screens all together
       program_name='Estadistica I',       # Defaults to script name
       program_description = 'Estadistica',       # Defaults to ArgParse Description
       default_size=(610, 530),   # starting size of the GUI
       required_cols=1,           # number of columns in the "Required" section
       optional_cols=2,           # number of columns in the "Optional" section
       dump_build_config=True   # Dump the JSON Gooey uses to configure itself
)
def main():
    parser = argparse.ArgumentParser(description="Programa para realizar calculos estadisticos")
    parser.add_argument("datos", type=str, default =0, action="store", help='Ingrese los datos aqui')
    parser.add_argument('-d','--decil', action="store", default=0, help="Ingrese el decil que desea calcular. "
                        "\nPara varios, por favor introduzcalos separados por un '-'. Ej: 1-2-7")
    parser.add_argument('-p','--percentil', action="store", default=0, help="Ingrese el percentil que desea calcular. "
                        "\nPara varios, por favor introduzcalos separados por un '-'. Ej: 10-20-73")
    parser.add_argument('-s','--sextil', action="store", default=0, help="Ingrese el sextil que desea calcular. "
                        "\nPara varios, por favor introduzcalos separados por un '-'. Ej: 1-2-5")
    parser.add_argument('-c','--cuartil', action="store", default=0, help="Ingrese el cuartil que desea calcular. "
                        "\nPara varios, por favor introduzcalos separados por un '-'. Ej: 1-2-3")
    parser.add_argument("-dq", "--desviacion_cuartilica", action="store_true", help='Seleccione si desea calcularla')
    parser.add_argument("-diq","--desviacion_intercuartilica", action="store_true", help='Seleccione si desea calcularla')
    parser.add_argument("-cv", "--coeficiente_de_variacion", action="store_true", help='Seleccione si desea calcularla')
    parser.add_argument("-vz", "--varianza", action="store_true", help='Seleccione si desea calcularla')
    parser.add_argument("-de", "--desviacion_estandar", action="store_true", help='Seleccione si desea calcularla')
    parser.add_argument("-cb", "--coeficiente_de_bowley", action="store_true", help='Seleccione si desea calcularla')
    parser.add_argument("-cp", "--coeficiente_de_pearson", action="store_true", help='Seleccione si desea calcularla')
    parser.add_argument("-k", "--curtosis", action="store_true", help='Seleccione si desea calcularla')
    args = parser.parse_args()
    dataStrings = args.datos
    numbers = dataStrings.split('-')
    lst = []
    for every_number in numbers:
        try:
            every_number = int(every_number)
            lst.append(every_number)
        except:
            TypeError

    objeto = Statistics()
    objeto.sum_numbers(lst)
    objeto.arithmetic_mean(lst)
    objeto.pow_numbers(lst)
    objeto.class_amplitude(lst)
    objeto.class_intervals(lst)
    objeto.class_marks()
    objeto.absolute_frequency(lst)
    objeto.relative_frequency(lst)
    objeto.print_table()
    print "La media aritmetica es ", objeto.arithmetic_mean(lst)
    objeto.geometric_mean(lst)
    objeto.median(lst)
    objeto.moda()

    def args_check(argument, test, A):
        dataStrings = argument
        if argument != 0:
            if dataStrings.find('-') != -1:
                tempLst = []
                dataStrings = dataStrings.split('-')
                for every_number in dataStrings:
                    every_number = int(every_number)
                    tempLst.append(every_number)
                for every_number in tempLst:
                    print test, every_number, " es ", objeto.measure_of_position(lst, A, every_number)
            else:
                dataStrings = int(dataStrings)
                print test, dataStrings, " es ", objeto.measure_of_position(lst, A, dataStrings)
    args_check(args.decil, "El decil ", 10)
    args_check(args.sextil, "El sextil ", 6)
    args_check(args.cuartil, "El cuartil ", 4)
    args_check(args.percentil, "El percentil ", 100)
    objeto.measures_of_dispersion(lst)
    if args.desviacion_cuartilica:
        objeto.quartile_deviation()
    if args.desviacion_intercuartilica:
        objeto.interquartile_deviation()
    if args.varianza:
        objeto.variance_func(lst)
    if args.desviacion_estandar:
        objeto.standard_deviation(lst)
    if args.coeficiente_de_variacion:
        objeto.variance_coefficient()
    if args.coeficiente_de_bowley:
        objeto.bowley_coefficient()
    if args.coeficiente_de_pearson:
        objeto.pearson_coefficient()
    if args.curtosis:
        objeto.kurtosis(lst)

main()
