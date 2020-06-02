from mip import *
from graf import *
from itertools import product

dataNode = buildDataNode()
dataEdge = buildDataEdge()

def solve() :
    m = int(input("Masukkan jumlah salesman : "))
    n = int(input("Masukkan jumlah kota tujuan :"))
    dest = [-1 for i in range(n)]
    for i in range(n) :
        dest[i] = int(input("Masukkan kota tujuan ke - " + str(i+1) + " : "))

    start = int(input("Masukkan tempat perusahaan : "))

    indeks, subgraph = buildSubgraph(dest, dataNode, dataEdge)
    print(subgraph)
    v = set(dest)

    model = Model()

    x = [[model.add_var(var_type=BINARY) for j in dest] for i in dest]


    model.objective = minimize(xsum(subgraph[i][j]*x[i][j] for i in range(len(dest)) for j in range(len(dest))))

    model += xsum(x[indeks[start]][indeks[j]] for j in v - {start} ) == m

    model += xsum(x[indeks[j]][indeks[start]] for j in v - {start} ) == m

    for i in dest :
        model += xsum(x[indeks[i]][indeks[j]] for j in v - {i} ) == 1
        

    for i in dest :
        model += xsum(x[indeks[j]][indeks[i]] for j in v - {i} ) == 1
        
    u = [model.add_var() for i in dest]

    p = n + 1


    for (i,j) in product(v - {start}, v - {start}) :
        if i != j :
            model += u[indeks[i]] - u[indeks[j]] + p*x[indeks[i]][indeks[j]] <= p - 1

    model.max_mip_gap_abs = 0.05
    # status = model.optimize(max_seconds=30,max_nodes = 100, max_solutions=1)
    status = model.optimize(max_seconds=30)
    print(status)

    print('route with total distances : ', end="")
    if status == OptimizationStatus.OPTIMAL :
        print(model.objective_value)
    elif status == OptimizationStatus.FEASIBLE :
        print(model.objective_value)
    else :
        print(model.objective_bound)

    route = []

    for i in range(len(dest)) :
        
        if x[indeks[start]][i].x >= 1 :
            print("ketemu", end=" ")
            route.append((start, dest[i]))
            node = dest[i]
            print(str(start) + " - ", end="")
            while node != start :
                print(str(node) + " - ", end="")
                for j in range(len(dest)) :
                    if x[indeks[node]][j].x >= 0.99 :
                        route.append((node, dest[j]))
                        node = dest[j]
                        break
            
            print(str(node))
            # while node != start :
            #     for j in range(len(dest)) :
            #         if x[start][]
    
    return route
