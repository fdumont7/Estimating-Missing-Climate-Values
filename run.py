#import v2ReadingExcelDoc
from FileInformation import FileInformation
from Estimate import Estimate

#v2ReadingExcelDoc.main()


FI = FileInformation()

E = Estimate()

print("AA =", E.AA(FI.getXi(), FI.getn()), "\nNormal Ratio =", E.NormalRatio(FI.getNs(), FI.getNi(), FI.getn(), FI.getXi()), "\nGC = ", E.GC(FI.getLongitude(), FI.getLatitude(), FI.getn(), FI.getXi()))



	