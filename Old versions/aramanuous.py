#  From Aramanuous 2020
# Armanuos, A. M., N. Al-Ansari and Z. M. Yaseen (2020). "Cross Assessment of Twenty-One Different Methods for Missing Precipitation Data Estimation." Atmosphere 11(4): 34.

import MATH


# n is the number of surrounding rain gauges
n = 4.0

# N is the average annual precipitation for rain gauge(i)
N1 = 43.33
N2 = 45.55
N3 = 42.42
N4 = 41.22
N5 = 40.37

#  x(i) is the precipitation for rain gauge(i) x5 is missing
x1 = 4.2
x2 = 3.8
x3 = 3.9
x4 = 4.0

# lat(i) and lon(i) are the latitude and longitude for rain gauge(i)
lat1 = 39.3531
lat2 = 39.1667
lat3 = 39.1033
lat4 = 39.3500
lat5 = 39.5167

lon1 = -84.2606
lon2 = -84.3000
lon3 = -84.4189
lon4 = -84.5833
lon5 = -84.4167

# d is the distance from rain gauge5 to rain gauge(i) as calculated by distance.py
d1 = 22.597600953658*1000
d2 = 40.1913268708822*1000
d3 = 46.3019543373498*1000
d4 = 23.4160574296991*1000

# Arithmetic Average
AA5 =(x1 + x2 + x3 + x4)/n
print("Arithmetic Average = ", AA5)

#  Normal Ratio
term1 = N5/N1 * x1
term2 = N5/N2 * x2
term3 = N5/N3 * x3
term4 = N5/N4 * x4

X5 = 1/n *(term1 + term2 + term3 + term4)

print('Normal Ratio = ', X5)

#  Geographic Coordinates
geoterm1 = 1/(lon1*lon1 + lat1*lat1)
geoterm2 = 1/(lon2*lon2 + lat2*lat2)
geoterm3 = 1/(lon3*lon3 + lat3*lat3)
geoterm4 = 1/(lon4*lon3 + lat4*lat4)

sumgeoterm = geoterm1 + geoterm2 + geoterm3 + geoterm4

geox1 = (geoterm1/sumgeoterm) * x1
geox2 = (geoterm2/sumgeoterm) * x2
geox3 = (geoterm3/sumgeoterm) * x3
geox4 = (geoterm4/sumgeoterm) * x4

sumgeo = geox1 + geox2 + geox3 + geox4

print('Geographical Coordinates = ', sumgeo)

#  Normal Ration with Geogrpahical Coordinates
annratiox1 = N5/N1 * geox1
annratiox2 = N5/N2 * geox2
annratiox3 = N5/N3 * geox3
annratiox4 = N5/N4 * geox4

sumannratio = annratiox1 + annratiox2 + annratiox3 + annratiox4

print('Normal ration with Geographical Coordinates = ', sumannratio)

#  Inverse Distance Weighting
weight1 = 1/(d1*d1)
weight2 = 1/(d2*d2)
weight3 = 1/(d3*d3)
weight4 = 1/(d4*d4)

sumweight = weight1 + weight2 + weight3 + weight4

idw1 = weight1/sumweight * x1
idw2 = weight2/sumweight * x2
idw3 = weight3/sumweight * x3
idw4 = weight4/sumweight * x4

sumidw = idw1 + idw2 + idw3 + idw4

print('Inverse Distance Weighting = ', sumidw)
