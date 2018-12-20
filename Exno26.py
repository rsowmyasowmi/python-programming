D = 7 
L = 3 
maxdev = [3,4,2]
allowed = [[1,3,7],[1,3,4,5,6,7],[2,4,5,6]]
problem = Problem()
problem.addVariables(["x_L%d_d%d" %(loc+1,d+1) for loc in range(L) for d in range(D) if d+1 in allowed[loc]],[0,1])
for loc in range(L):
    problem.addConstraint(MaxSumConstraint(maxdev[loc]),["x_L%d_d%d" %(loc+1,d+1) for d in range(D) if d+1 in allowed[loc]])
for d in range(D):
    problem.addConstraint(ExactSumConstraint(1),["x_L%d_d%d" %(loc+1,d+1) for loc in range(L) if d+1 in allowed[loc]])
S = problem.getSolutions()
n = len(S)
n
