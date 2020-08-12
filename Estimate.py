#Ns = mean of available rainfall at the target station. Should be a float
#Ni= mean of the available rainfall data at the ith surrounding stations. Should be a list.
#n= surrounding stations. Should be a float
#Xi= measured value of the climatic parameter in the surrounding stations. Should be a list
#xi= Longitude of the ith nearby station. should be a list
#yi= Latitude of the ith neaby station. should be a list

class Estimate:

	#Simple Arithmetic Average
	def AA(Xi, n):
		return sum(Xi)/n

	
	def NormalRatio(self,Ns, Ni, n, Xi):
		num = 0
		fullSum = 0
		for i in Xi:
			fullSum = fullSum + (Ns/Ni[num])*i
			num = num + 1
		Yi = (1/n)*fullSum
		return Yi

	def GC(xi, yi, n, Xi):
		num = 0
		fullSum = 0
		bottumSum = 0
		for i in xi:
				bottumSum = bottumSum + (1/(i**2 * yi[num]**2))
				num = num + 1

		num = 0
		for i in Xi:
			fullSum = fullSum + ((1/(xi[num]**2 * yi[num]**2))/bottumSum)*i
			num = num + 1

		Yi = fullSum
		return Yi


