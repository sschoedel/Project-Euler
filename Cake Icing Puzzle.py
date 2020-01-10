import numpy as np
from itertools import cycle
a = 9
b = 10
c = 11
x = 360/a
y = 360/b
z = 360/np.sqrt(c)
# initial icing amount
totalIcing = 360
totalCake = 0
prevLocation = 0
numRotations = 0

switches = []  # switches appear where icing and cake touch
icing = []
# starts as 0-360 is all icing where 0 and 360 are connected so switches = []
# after first x flip, 0-40 is cake and 40-360 is icing so switches = [0, 40, 360]
# and icing = [0, 1] where 0 corresponds to 0-40 and 1 corresponds to 40-0 (360=0)

def testForIcing(nextLocation):
	for i in range(len(switches)):
		if nextLocation > i and nextLocation < i + 1:

	return icing

cont = True
while cont:
	nextLocation = prevLocation + x
	if nextLocation > 360:
		flipAmount = 360 - prevLocation
		inverseAmount = x - flipAmount
	else:
		flipAmount = x
		inverseAmount = 0
	if icing:
		totalIcing -= flipAmount
		totalIcing += inverseAmount

		totalCake -= inverseAmount
		totalCake += flipAmount
