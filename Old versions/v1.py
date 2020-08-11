#  Normal Ratio
#  Aramanuous 2020 equation 3

import math
N = [43.33,45.55,42.42,41.22,40.37]
x = [4.2,3.8, 3.9, 4.0]
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
