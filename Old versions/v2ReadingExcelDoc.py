import xlrd #whats used to read excel document. get by 'pip install xlrd'

def main():
	fileLocation = getFile()	
	X5 = calculate(getN(fileLocation), getx(fileLocation))
	print("X5 =",X5)


def getFile():
	while True:
		try:
			fileLocation = input("What file would you like to open (please put in full location)\n")
			workBook = xlrd.open_workbook(fileLocation)
			
			break
		except OSError:
			print("invalid file name please try again")
	return fileLocation

#Parameters are both lists
def calculate(N, x):
	term = []
	num = 0
	for i in x:
	    term.append(N[-1]/N[num] * i)
	    num=num+1

	n = 5.0
	termSum=0
	for i in term:
	    termSum= termSum + i

	X5 = 1/n * termSum
	return X5


def getN(fileLocation):
	workBook = xlrd.open_workbook(fileLocation)
	sheet = workBook.sheet_by_index(0)
	N = sheet.row_values(0)[1:]
	return N


def getx(fileLocation):
	workBook = xlrd.open_workbook(fileLocation)
	sheet = workBook.sheet_by_index(0)
	x = sheet.row_values(1)[1:]
	x.remove('')
	return x


