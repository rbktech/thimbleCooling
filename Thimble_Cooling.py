import numpy as np

#Setting the parameters of the model
a = 1.0
b = 1.0
c = 1.0
d = 0.0

# Setting up the action of the model
def RealAction(x,y):
 RealAction = b*(3*(x**3)*y - 3*x*(y**3))/4 + a*(x**4 + y**4 - 6*(x**2)*(y**2))/4 + d*(2*x*y)/2 + c*(x**2 - y**2)/2
 return RealAction

def ImaginaryAction(x,y):
 ImaginaryAction = a*(3*(x**3)*y - 3*x*(y**3))/4 + b*(x**4 + y**4 - 6*(x**2)*(y**2))/4 + c*(2*x*y)/2 + d*(x**2 - y**2)/2
 return ImaginaryAction

# Choosing the critical point of the action
RealCritical = 0.0
ImaginaryCritical = 0.0


# Distance function, defined as the absolute value of the difference between the 
# imaginary part of the action at a random point, and imaginary part of the action
# at the critical point
def DistanceFunctionM(x,y):
	distance = (abs(ImaginaryAction(x,y) - ImaginaryAction(RealCritical,ImaginaryCritical)))**2
	return distance

# Derivatives of the distance function, defined for determining the next step
def xDerivativeDistanceFunctionM(x,y):
	derValue = 2*(abs(ImaginaryAction(x,y) - ImaginaryAction(RealCritical,ImaginaryCritical)))*(a*(9*(x**2)*y - 3*(y**3))/4 + b*(4*(x**3) - 12*x*(y**2))/4 + c*(2*y)/2 + d*(2*x)/2)
	return derValue

def yDerivativeDistanceFunctionM(x,y):
	derValue = 2*(abs(ImaginaryAction(x,y) - ImaginaryAction(RealCritical,ImaginaryCritical)))*(a*(3*x**3 - 9*x*y**2)/4 + b*(4*y**3 - 12*x**2*y)/4 + c*(2*x)/2 + d*(- 2*y)/2)
	return derValue

# To determine if the point belongs on a thimble or an anti-thimble
# True means it is thimble. False means it is anti-thimble
def thimbleOrNotThimble(x,y):
	if RealAction(x,y)>RealAction(RealCritical,ImaginaryCritical):
		return True 
	return False

# The set of points corresponding to thimbles and anti-thimbles
thimblePoints = [(RealCritical,ImaginaryCritical)]
antiThimblePoints = [(RealCritical,ImaginaryCritical)]

initialPoints = [((RealCritical,ImaginaryCritical))]

# Setting up the evolution, with numberOfPoints number of points
numberOfPoints = 5
stepSize = 0.1
tolerance = 0.0001 #how close you want the point to lie near the curve
squareSize = 10 # size of the square of random points

for i in range(numberOfPoints):
	x = 2*squareSize*np.random.random_sample() - squareSize # gives random values of x in the range (-squareSize,squareSize)
	y = 2*squareSize*np.random.random_sample() - squareSize
	initialPoints.append((x,y))
	while(DistanceFunctionM(x,y)>tolerance):
		Dx = xDerivativeDistanceFunctionM(x,y)
		Dy = -1 * yDerivativeDistanceFunctionM(x,y)
		x = x + Dx*stepSize
		y = y + Dy*stepSize
	if thimbleOrNotThimble(x,y):
		thimblePoints.append((x,y))
	else:
		antiThimblePoints.append((x,y))

print thimblePoints,antiThimblePoints #This is temporary. Need to add code to plot these points and see what is happening