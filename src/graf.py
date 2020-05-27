import queue as Q

def buildDataNode() :
    dataNode = open('../assets/OLcnode.txt', 'r')
    nodes = dataNode.readlines()
    
    data = {}

    for node in nodes :
        node = node.split(' ')
        if node[2][-1] == '\n' :
            node[2] = node[2][:-1]
        data[node[0]] = (float(node[1]), float(node[2]))
    
    return data

def buildDataEdge() :
    dataEdge = open('../assets/OLcedge.txt', 'r')
    edges = dataEdge.readlines()

    data = {}

    for edge in edges :
        edge = edge.split(' ')
        
        if edge[1] not in data : 
            data[edge[1]] = []
        if edge[2] not in data :
            data[edge[2]] = []
        
        if edge[3][-1] == '\n' : 
            edge[3] = edge[3][:-1]
        data[edge[1]].append((edge[2], float(edge[3])))

        # asumsi jalanan 2 arah
        data[edge[2]].append((edge[1], float(edge[3])))
    
    return data

def buildSubgraph(listNode, dataNode, dataEdge) :
    indeks = {}
    for i in range(len(listNode)) : 
        indeks[listNode[i]] = i

    subgraph = [[-1 for i in range(len(listNode))] for j in range(len(listNode))]

    for i in range(len(listNode)) :
        for j in range(i, len(listNode)) :
            if i != j : 
                subgraph[indeks[i]][indeks[j]] = dijkstra(i, j, dataNode, dataEdge)
    
    return indeks, subgraph

def dijkstra(src, end, dataNode, dataEdge) :
    pq = Q.PriorityQueue()
    dist = {}
    for data in dataNode :
        dist[data] = float('inf')
    
    dist[src] = 0
    pq.put((0, src))
    while not pq.empty() :
        u = pq.get()[1]
        for i in range(len(dataEdge[u])) :
            adj = dataEdge[u][i][0]
            weight = dataEdge[u][i][1]

            if dist[adj] > dist[u] + weight :
                dist[adj] = dist[u] + weight
                pq.put((dist[adj], adj))

    return dist[end]


# dataNode = buildDataNode()
# dataEdge = buildDataEdge()
# dijkstra(1,2, dataNode, dataEdge)
            
