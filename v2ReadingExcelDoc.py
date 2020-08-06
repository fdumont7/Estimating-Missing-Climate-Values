import xlrd #reads excel doc need to pip install xlrd

loc = input("What file would you like to open (please put in full location)\n")

#open workbook and sheet
workBook = xlrd.open_workbook(loc)
sheet = workBook.sheet_by_index(0)

#print data
N = sheet.row_values(0)[1:]

print(N)
x = sheet.row_values(1)[1:]
x.remove('')
print(x)

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

print("X5 =",X5)