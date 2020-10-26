#Ns = mean of available rainfall at the target station. Should be a float
#Ni= mean of the available rainfall data at the ith surrounding stations. Should be a list.
#n= surrounding stations. Should be a float
#Xi= measured value of the climatic parameter in the surrounding stations. Should be a list
#xi= Longitude of the ith nearby station. should be a list
#yi= Latitude of the ith neaby station. should be a list

class Estimate:

	#Simple Arithmetic Average
	def AA(self, Xi, n):
		return sum(Xi)/n

	
	def NormalRatio(self,Ns, n,  Ni, Xi):
		num = 0
		fullSum = 0
		for i in Xi:
			fullSum = fullSum + (Ns/Ni[num])*i
			num = num + 1
		Yi = (1/n)*fullSum
		return Yi


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

	def CCW(self, ri, Xi):
		fullSum = 0
		num = 0
		bottomSum = sum(ri)

		for i in ri:
			fullSum = fullSum + (i/bottomSum)*Xi[num]
			num = num + 1

		Yi = fullSum
		return Yi


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










	




