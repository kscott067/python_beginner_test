
def solve_y(m, x, b):
	solution = m*x+b
	return solution
yvar = solve_y(2,3,8)
print("This is your y variable: "+str(yvar)+" .")

def solve_x(y, b, m):
	solution = (y-b)/m
	return solution
xvar = solve_x(yvar, 8, 2)
print("This is your x variable: "+str(xvar)+" .")

def solve_m(y, b, x):
	solution = (y-b)/x
	return solution
mvar = solve_m(yvar, 8, xvar)
print("This is your m variable: "+str(mvar)+" .")

def solve_b(y, m, x):
	solution = y-m*x
	return solution
bvar = solve_b(yvar, mvar, xvar)
print("This is your b variable: "+str(bvar)+" .")