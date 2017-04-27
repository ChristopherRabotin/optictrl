import numpy as np

# Create the A, B and C matrices
n = 100
N = 20
m = 50
mu = 1/200.
gamma = np.ones(n)

def aij():
    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                yield 0.5
            elif j == i+1:
                yield 0.25
            elif j == i-1:
                yield -0.25
            else:
                yield 0.0

A = np.fromiter(aij(), dtype=float).reshape(n, n)

def b_or_c_ij(forC=False):
    for i in xrange(n):
        for j in xrange(m):
            yield (int(forC) * mu) * (float(i) - (int(forC) * -1) * float(j))/(n + m)

B = np.fromiter(b_or_c_ij(), dtype=float).reshape(n, m)

C = np.fromiter(b_or_c_ij(True), dtype=float).reshape(n, m)

# Build the histories
x_history = [np.zeros(n)]
u_history = [np.zeros(m)]
for t in xrange(N-1):
    xt = x_history[t]
    ut = u_history[t]
    x_history.append(np.dot(A, xt) + np.dot(B, ut) + np.dot(np.dot(xt.transpose(), np.dot(C, ut)), gamma))
    u_history.append(np.zeros(m)) # Oddly this is only zeros.

def pb1_cost():
    J = 0.0
    for t in xrange(N-1):
        expression1 = 0.0
        for i in xrange(n):
            expression1 += np.power((x_history[t][i] + 0.25), 4)
        expression2 = 0.0
        for j in xrange(m):
            expression2 += np.power((u_history[t][j] + 0.5), 4)
        J += expression1 + expression2
    for i in xrange(n):
        J += np.power((x_history[-1][i] + 0.25), 4)
    return J
