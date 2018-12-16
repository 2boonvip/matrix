import numpy as np
np.set_printoptions(linewidth=200)

A = 250
d = np.array([[0,20,70,10],
              [20,0,40,20],
              [70,40,0,30],
              [10,20,30,0]])

Q = np.zeros((20,20))

for i in range(4):
    for j in range(4):
        for k in range(4):
            Q[5*i+k][5*j+k] = 4 * A
            Q[5*i+k][5*j+k+1] = d[i][j]
        
for i in range(4):
    for j in range(4):
        Q[5*i+j][5*i+j] = 2 * A
        
print(Q)