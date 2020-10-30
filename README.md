# Normal-Ratio
### To setup in command prompt with python installed:

-change directory to Estimating-Missing-Climate-Values.
-type: pip install xlrd.


### to setup in pycharm:

-bring up project in pycharm.
-go to settings-> project interpreter.
-press the plus button on the right.
-search for xlrd and install the package.


#### to run in command prompt with python installed:
-type: py run.py

### to run in pycharm:
-find run.py in the project explorer
-right click run.py and click run 'run'

### format for the excel document:
|     |     |     |      |      |
| --- | --- | --- | --- | --- |
| N	| # | # | # | ... |
| X | # | # | # | ... |
| longitude |	# | # | # | ... |
| latitude | # | # | # | ... |
| di | # | # | # | ... |
| k |	# |
| hi | # | # | # | ... |
| ri |# | # | # | ... |



N= mean of the available rainfall data at the ith surrounding stations. Should be a list.

X= measured value of the climatic parameter in the surrounding stations. Should be a list

longitude = Longitude of the ith nearby station. should be a list

latitude = Latitude of the ith neaby station. should be a list

di= Distance from teh target station to the ith surrounding station

k= distance of frictionv varying from 1 to 6

hi= absolute value of difference in elevation between the target and surrounding station

ri= pearsons correlation coefficient between the target station and each neighboring station

See testdoc.xlsx for example of the proper format



