import queue as Q
from math import *

def buildDataNode() :
    dataNode = open('../assets/OLcnode.txt', 'r')
    nodes = dataNode.readlines()
    
    data = {}

    for node in nodes :
        node = node.split(' ')
        if node[2][-1] == '\n' :
            node[2] = node[2][:-1]
        data[int(node[0])] = (float(node[1]), float(node[2]))
    
    return data

def buildDataEdge() :
    dataEdge = open('../assets/OLcedge.txt', 'r')
    edges = dataEdge.readlines()

    data = {}

    for edge in edges :
        edge = edge.split(' ')
        
        if int(edge[1]) not in data : 
            data[int(edge[1])] = []
        if int(edge[2]) not in data :
            data[int(edge[2])] = []
        
        if edge[3][-1] == '\n' : 
            edge[3] = edge[3][:-1]
        data[int(edge[1])].append((int(edge[2]), float(edge[3])))

        # asumsi jalanan 2 arah
        data[int(edge[2])].append((int(edge[1]), float(edge[3])))
    
    return data

def buildSubgraph(listNode, dataNode, dataEdge) :
    indeks = {}
    for i in range(len(listNode)) :
        indeks[listNode[i]] = i
    subgraph = [[0 for i in range(len(listNode))] for j in range(len(listNode))]

    routes = [[ [] for i in range(len(listNode))] for j in range(len(listNode))]
    parent = {}

    for i in range(len(listNode)) :
        for j in range(len(listNode)) :
            if i < j : 
                dist, route = dijkstra(listNode[i], listNode[j], dataNode, dataEdge)
                subgraph[i][j] = dist
                routes[i][j] = route
            elif i > j :
                subgraph[i][j] = subgraph[j][i]
                routes[i][j] = routes[j][i]
    
    return indeks, subgraph, routes

def dijkstra(src, end, dataNode, dataEdge) :
    pq = Q.PriorityQueue()
    dist = {}
    parent = {}
    for data in dataNode :
        parent[data] = -1
        dist[data] = float('inf')

    parent[src] = src
    dist[src] = 0
    pq.put((0, src))
    while not pq.empty() :
        u = pq.get()[1]

        for i in range(len(dataEdge[u])) :
            adj = dataEdge[u][i][0]
            weight = dataEdge[u][i][1]

            if dist[adj] > dist[u] + weight :
                parent[adj] = u
                dist[adj] = dist[u] + weight
                pq.put((dist[adj], adj))
    
    visit = end
    route = [(parent[visit], visit)]
    while(parent[visit] != src) :
        visit = parent[visit]
        route.append((parent[visit], visit))
    
    return dist[end], route

def gradien(p1, p2, dataNode) :
    x1, y1 = dataNode[p1][0], dataNode[p1][1]
    x2, y2 = dataNode[p2][0], dataNode[p2][1]

    result = (y2 - y1)/(x2 - x1)
    return result

def split(src, listNode, m, dataNode) :
    copyListNode = []
    for x in listNode :
        copyListNode.append(x)
    
    copyListNode.remove(src)
    newList = [(gradien(src, copyListNode[i], dataNode),copyListNode[i]) for i in range(len(copyListNode))]

    jumlah = len(copyListNode)
    div = floor(jumlah / m)
    if jumlah%m != 0 :
        div += 1
    
    newList.sort()
    # print(div)
    # print(newList)
    newListNode = [[] for i in range(m)]
    i = 0
    j = 0
    count = 0
    while i < jumlah :
        newListNode[count].append(newList[i][1])
        i += 1
        j += 1
        if j == div :
            j = 0
            count += 1
    
    for x in newListNode :
        x.append(src)

    return newListNode

# print(split(1,[2,3,4,5,6,7,8], 3, buildDataNode()))
        

# dataNode = buildDataNode()
# dataEdge = buildDataEdge()
# dijkstra(1,2, dataNode, dataEdge)
            
