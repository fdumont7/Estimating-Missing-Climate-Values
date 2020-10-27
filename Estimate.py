#Author: Faryn Dumont

#Equations taken from "Cross Assessment of Twenty-One different Methods for Missing Precipitaiton Data Estimation" by Asaad M. Armanuos, Nadhir Al-Ansari and Zaher Mudher Yaseen

#Ns = mean of available rainfall at the target station. Should be a float
#Ni= mean of the available rainfall data at the ith surrounding stations. Should be a list.
#n= surrounding stations. Should be a float
#Xi= measured value of the climatic parameter in the surrounding stations. Should be a list
#xi= Longitude of the ith nearby station. should be a list
#yi= Latitude of the ith neaby station. should be a list
#di= Distance from teh target station to the ith surrounding station
#k= distance of frictionv arying from 1 to 6
#hi= absolute value of difference in elevation between the target and surrounding station
#ri= pearsons correlation coefficient between the target station and each neighboring station

class Estimate:

	#2.1.1 Simple Arithmetic Average
	def AA(self, Xi, n):
		return sum(Xi)/n

	#2.1.2 Normal Ratio
	def NR(self,Ns, n,  Ni, Xi):
		num = 0
		fullSum = 0
		for i in Xi:
			fullSum = fullSum + (Ns/Ni[num])*i
			num = num + 1
		Yi = (1/n)*fullSum
		return Yi

	#2.1.3 Geographical Coordinates
	def GC(self,xi, yi, Xi):
		num = 0
		fullSum = 0
		bottomSum = 0
		for i in xi:
			bottomSum = bottomSum + (1/(i**2 * yi[num]**2))
			num = num + 1

		num = 0
		for i in Xi:
			fullSum = fullSum + ((1/(xi[num]**2 * yi[num]**2))/bottomSum)*i
			num = num + 1

		Yi = fullSum
		return Yi

	#2.1.4 Normal Ratio with Geographical Coordinates
	def NRGC(self, Ns, Ni, Xi, xi, yi):
		num = 0
		fullSum = 0
		bottomSum = 0
		for i in xi:
			bottomSum = bottomSum + (1/(i**2 * yi[num]**2))
			num = num + 1

		num = 0
		for i in Xi:
			fullSum = fullSum + ((1/(xi[num]**2 * yi[num]**2))*(Ns/Ni[num]))/(bottomSum*(Ns/Ni[num]))*i

		Yi = fullSum
		return Yi

	#2.1.5 Inverse Distance Weighting 
	def IDW(self, di, k, Xi):
		fullSum = 0
		bottomSum = 0
		num = 0

		for i in di:
			bottomSum = bottomSum + 1/(i**k)

		for i in di:
			fullSum = fullSum + ((1/i**k)/bottomSum)*Xi[num]
			num = num + 1 

		Yi = fullSum
		return Yi

	#2.1.6 Modified Inverse Distance Weighting
	def MIDW(self,di, hi, k, Xi):
		fullSum = 0
		bottomSum = 0
		num = 0

		for i in di:
			bottomSum = bottomSum + (1/(hi[num]**k * i**k))
			num = num + 1


		num = 0

		for i in di:
			fullSum = fullSum + ((1/(hi[num]**k * i**k))/bottomSum)*Xi[num]
			num = num + 1

		Yi = fullSum
		return Yi

	#2.1.7 Correlation coefficient Weighted
	def CCW(self, ri, Xi):
		fullSum = 0
		num = 0
		bottomSum = sum(ri)

		for i in ri:
			fullSum = fullSum + (i/bottomSum)*Xi[num]
			num = num + 1

		Yi = fullSum
		return Yi

	#2.1.18 Modified Old Normal Ratio with Inverse Distance
	def ONRID(self, Ns, Ni, di, Xi):
		fullSum = 0
		num = 0
		bottomSum = 0

		for i in Ni:
			bottomSum = bottomSum + ((Ns/i)*di[num]**-2)
		num = 0 
		for i in Ni:
			fullSum = fullSum + (((Ns/i)*di[num]**-2)/bottomSum)*Xi[num]

		Yi = fullSum
		return Yi










	




