import xlrd #whats used to read excel document. get by 'pip install xlrd'

myFile = ""
workBook = ""

class FileInformation:

	def __init__(self, afile):
		myFile = afile
		try:
			workBook = xlrd.open_workbook(myFile)
			break
		except OSError:
			print("invalid file name")

		workBook = xlrd.open_workbook(myFile)
	#Xi = measured value of the climatic parameter in the surrounding stations
	#returns a list
	def getXi:
		sheet = workBook.sheet_by_index(0)
		x = sheet.row_values(1)[1:]
		x.remove('')
		return x

	#n = number of surrounding stations.
	def getn:
		sheet = workBook.sheet_by_index(0)
		return sheet.nrows

	#mean of the available rainfall
	#returns a list
	def getNs:
		sheet = workBook.sheet_by_index(0)
		N = sheet.row_values(0)[1:]
		return N

	#mean of the available rainfall data at the ith surrounding stations
	#returns a float
	def getNi:
		return float(getNs[-1])


	#longitude of the ith nearby station
	def getLongitude:
		sheet = workBook.sheet_by_index(0)
		longitude = sheet.row_values(2)[1:]
		return longitude

	#latitude of the ith nearby station
	def getLatitude:
		sheet = workBook.sheet_by_index(0)
		latitude = sheet.row_values(3)[1:]
		return latitude

	#distance from the target station to the ith surrounding station
	def getdi:
		sheet = workBook.sheet_by_index(0)
		di = sheet.row_values(4)[1:]
		return di

	#distance of friction varying from 1 to 6
	#returns int k
	#may need a set k function as well idk where k is held
	def getk:
		sheet = workBook.sheet_by_index(0)
		k = sheet.row_values(3)[1]
		return k

		
