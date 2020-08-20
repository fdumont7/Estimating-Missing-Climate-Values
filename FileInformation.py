import xlrd #whats used to read excel document. get by 'pip install xlrd'
import math
#currently the target station is the last item in the document.
class FileInformation:

	def __init__(self):
		
		while True:
			try:
				myFile = input("What file would you like to open (please put in full location)\n")
				workBook = xlrd.open_workbook(myFile)
				
				break
			except OSError:
				print("invalid file name please try again")

		self.workBook = xlrd.open_workbook(myFile)
		self.sheet = workBook.sheet_by_index(0)
		

	#Xi = measured value of the climatic parameter in the surrounding stations
	#returns a list
	def getXi(self):
		x = self.sheet.row_values(1)[1:]
		x.remove('')
		return x

	#n = number of surrounding stations.
	def getn(self):
		return self.sheet.nrows

	#mean of the available rainfall at the target station
	#returns a float
	def getNs(self):
		return float(self.getNi()[-1])
		

	#mean of the available rainfall data at the ith surrounding stations
	#returns a list
	def getNi(self):
		N = self.sheet.row_values(0)[1:]
		return N

	#longitude of the ith nearby station
	def getLongitude(self):
		longitude = self.sheet.row_values(2)[1:]
		return longitude

	#latitude of the ith nearby station
	def getLatitude(self):
		latitude = self.sheet.row_values(3)[1:]
		return latitude

	#distance from the target station to the ith surrounding station
	#assuming target station is last on the list.
	def getdi(self):
		myLong = getLongitude()
		myLat = getLatitude()
		targetLong = radians(myLong[-1])
		targetLat = radians(myLat[-1])
		for i in myLong:
			i = radians(i)
		for i in myLat:
			i = radians(myLat[i])



		return di

	#distance of friction varying from 1 to 6
	#returns int k
	#may need a set k function as well idk where k is held
	def getk(self):
		k = self.sheet.row_values(3)[1]
		return k




		
