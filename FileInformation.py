import xlrd #whats used to read excel document. get by 'pip install xlrd'


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
		#x.remove('')
		return x

	#n = number of surrounding stations.
	def getn(self):
		
		return self.sheet.nrows

	#mean of the available rainfall
	#returns a list
	def getNs(self):
		
		return float(self.getNi()[-1])
		

	#mean of the available rainfall data at the ith surrounding stations
	#returns a float
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
	def getdi(self):
		
		di = self.sheet.row_values(4)[1:]
		return di

	#distance of friction varying from 1 to 6
	#returns int k
	def getk(self):
		
		k = self.sheet.row_values(5)[1]
		return k

	#absolute value of difference in elevation between the target and surrounding station
	def gethi(self):
		hi = self.sheet.row_values(6)[1:]
		return hi

	#pearsons correlation coefficient between the target station and each neighboring station
	def getri(self):
		ri = self.sheet.row_values(7)[1:]
		return ri


		
