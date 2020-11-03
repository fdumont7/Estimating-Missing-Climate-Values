#import v2ReadingExcelDoc
from FileInformation import FileInformation
from Estimate import Estimate


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

print("AA =", AA , "\nNormal Ratio =", NR , "\nGC = ", GC, "\nNRGC =", NRGC, "\nIDW =", IDW , "\nMIDW =", MIDW, "\nCCW =", CCW , "\nONRID =", ONRID)



	
