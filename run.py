#import v2ReadingExcelDoc
from FileInformation import FileInformation
from Estimate import Estimate
import csv


FI = FileInformation()

E = Estimate()

AA = E.AA(FI.getXi(), FI.getn())

NR = E.NR(FI.getNs(), FI.getn(), FI.getNi(), FI.getXi())

GC = E.GC(FI.getLongitude(), FI.getLatitude(),  FI.getXi())

NRGC = E.NRGC(FI.getNs(), FI.getNi(), FI.getXi(), FI.getLongitude(), FI.getLatitude())

IDW = E.IDW(FI.getdi(), FI.getk(), FI.getXi())

MIDW = E.MIDW(FI.getdi(), FI.gethi(), FI.getk(), FI.getXi())

CCW = E.CCW(FI.getri(), FI.getXi())

ONRID = E.ONRID(FI.getNs(), FI.getNi(), FI.getdi(), FI.getXi())

print("AA =", AA , "\nNR =", NR , "\nGC = ", GC, "\nNRGC =", NRGC, "\nIDW =", IDW , "\nMIDW =", MIDW, "\nCCW=", CCW , "\nONRID =", ONRID)

writetofile = input("\nWould you like to print to a file? (Y/N)")

if writetofile == "Y":
	fields = ["Equation used", "Result"]
	rows = [["Simple Arithmetic Average", AA],
		   ["Normal Ratio", NR],
		   ["Geographical Coordinates", GC],
		   ["Normal Ratio with Geographical Coordinates", NRGC],
		   ["Inverse distance Weighting", IDW],
		   ["Modified Inverse Distance Weighting", MIDW],
		   ["Correlation Coefficient Weighted", CCW],
		   ["Modified Old Normal Ratio with Inverse Distance", ONRID]]
	fileName = "Estimated-Values.csv"
	with open(fileName, 'w') as csvfile:  
		# creating a csv writer object  
		csvwriter = csv.writer(csvfile)  
		    
		# writing the fields  
		csvwriter.writerow(fields)  
		    
		# writing the data rows  
		csvwriter.writerows(rows) 


	
