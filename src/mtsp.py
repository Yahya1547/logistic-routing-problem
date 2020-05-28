from mip import *
from graf import *
from itertools import product

dataNode = buildDataNode()
dataEdge = buildDataEdge()

m = int(input("Masukkan jumlah salesman : "))
n = int(input("Masukkan jumlah kota tujuan :"))
dest = [-1 for i in range(n)]
for i in range(n) :
    dest[i] = int(input("Masukkan kota tujuan ke - " + str(i+1) + " : "))

start = int(input("Masukkan tempat perusahaan : "))

subgraph = buildSubgraph(dest, dataNode, dataEdge)
print(subgraph)
model = Model()

x = [[model.add_var(var_type=BINARY) for j in dest] for i in dest]

model += xsum(x[start][j] for j in range(len(dest))) == m

model += xsum(x[j][start] for j in range(len(dest))) == m

for i in range(len(dest)) :
    model += xsum(x[i][j] for j in range(len(dest)) if dest[j] != m) == 1
    

for i in range(len(dest)) :
    model += xsum(x[j][i] for j in range(len(dest)) if dest[j] != m) == 1
    
u = [model.add_var() for i in dest]

p = n + 2 - m

model.objective = minimize(xsum(subgraph[i][j]*x[i][j] for i in range(len(dest)) for j in range(len(dest))))
for (i,j) in product(range(len(dest)), range(len(dest))) :
    if i != j and dest[i] != m and dest[j] != m:
        model += u[i] - u[j] + p*x[i][j] <= p - 1

model.optimize(max_seconds=30)

if model.num_solutions :
    print('route with total distances : ' + str(model.objective_value))








