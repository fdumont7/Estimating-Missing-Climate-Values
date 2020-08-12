#import v2ReadingExcelDoc
from FileInformation import FileInformation
from Estimate import Estimate

#v2ReadingExcelDoc.main()


FI = FileInformation()

E = Estimate()

print(E.NormalRatio(FI.getNs, FI.getNi, FI.getn, FI.getXi))



	