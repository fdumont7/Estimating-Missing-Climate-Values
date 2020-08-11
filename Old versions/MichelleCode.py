#  Normal Ratio
#  Aramanuous 2020 equation 3

import math

N1 = 43.33
N2 = 45.55
N3 = 42.42
N4 = 41.22
N5 = 40.37

x1 = 4.2
x2 = 3.8
x3 = 3.9
x4 = 4.0

term1 = N5/N1 * x1
term2 = N5/N2 * x2
term3 = N5/N3 * x3
term4 = N5/N4 * x4

n = 5.0

X5 = 1/n *(term1 + term2 + term3 + term4)

print("X5 =",X5)
