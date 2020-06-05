from mip import *
from graf import *

from itertools import product


def solve(dataNode, dataEdge) :
    m = int(input("Masukkan jumlah salesman : "))
    n = int(input("Masukkan jumlah kota tujuan :"))
    dest = [-1 for i in range(n)]
    for i in range(n) :
        dest[i] = int(input("Masukkan kota tujuan ke - " + str(i+1) + " : "))

    start = int(input("Masukkan tempat perusahaan : "))

    solutions = [-1 for i in range(m)]
    solution_routes = [[] for i in range(m)]

    listNode = split(start, dest, m, dataNode)
    print(listNode)
    for k in range(m) :
        destination = listNode[k]
        n = len(destination)
        indeks, subgraph, routes = buildSubgraph(destination, dataNode, dataEdge)
        print(subgraph)
        print(indeks)
        v = set(destination)

        # building model
        model = Model()

        x = [[model.add_var(var_type=BINARY) for j in destination] for i in destination]
        u = [model.add_var() for i in destination]

        # adding constraints to the model
        model.objective = minimize(xsum(subgraph[i][j]*x[i][j] for i in range(len(destination)) for j in range(len(destination))))

        model += xsum(x[indeks[start]][indeks[j]] for j in v - {start} ) == 1

        model += xsum(x[indeks[j]][indeks[start]] for j in v - {start} ) == 1

        for i in destination :
            model += xsum(x[indeks[i]][indeks[j]] for j in v - {i} ) == 1
        
        for i in destination :
            model += xsum(x[indeks[j]][indeks[i]] for j in v - {i} ) == 1
        
        p = n + 1

        for (i,j) in product(v - {start}, v - {start}) :
            if i != j :
                model += u[indeks[i]] - u[indeks[j]] + p*x[indeks[i]][indeks[j]] <= p - 1

        # model.max_mip_gap_abs = 0.05
        status = model.optimize(max_seconds=30)

        # find the solution
        solutions[k] = model.objective_value
        print("solution " + str(k+1) + " : " + str(model.objective_value))

        # setting up the route for the solution from mip solver
        route = []
        for i in range(len(destination)) :
            if x[indeks[start]][i].x >= 1 :
                route.append((start, destination[i], routes[indeks[start]][i]))
                node = destination[i]

                while node != start :

                    for j in range(len(destination)) :
                        if x[indeks[node]][j].x >= 0.99 :
                            route.append((node, destination[j], routes[indeks[node]][j]))
                            node = destination[j]
                            break
        
                break
        solution_routes[k] = route

    return solutions, solution_routes, dest

