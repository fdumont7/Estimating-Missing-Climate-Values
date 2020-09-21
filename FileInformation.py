import xlrd #whats used to read excel document. get by 'pip install xlrd'


class FileInformation:

	def __init__(self):
		self.data = getData(input("What file would you like to open (please put in full location)\n"))
		while self.data == 0:
			print("invalid file name please try again")
			self.data = getData(input("What file would you like to open (please put in full location)\n"))
		
		

	
	def getData(self, file):
		if ".xlsx" in file:
			workBook = xlrd.open_workbook(file, on_demand = True)
			sheet = workBook.sheet_by_index(0)
			data = []
			#station ID
			data.append(sheet.col_values(0))
			#Year
			data.append(sheet.col_values(2))
			#month
			data.append(sheet.col_values(3))
			#Day
			data.append(sheet.col_values(4))
			#Hour
			data.append(sheet.col_values(5))
			#Precipitation data
			data.append(sheet.col_values(6))
			return data
		else if ".dat" in file:

		else:
			return 0
		

	

		
