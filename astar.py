graph={'a':(['b', 'e'], 11, [2, 3]),
'b':(['a', 'c', 'g'], 6, [2, 1, 9]),
'c':(['b'], 99, [2, 3]),
'd':(['e', 'g'], 1, [6, 1]),
'e':(['a', 'd'], 7, [3, 6]),
'g':(['b', 'd'], 0, [9, 1])
}

minpc=float('inf')
minpath=[]

def getPathcost(graph, a, b):
    ind=graph[a][0].index(b)
    return graph[a][2][ind]

def totalPathcost(path):
    pathcost=0
    for i in range(1, len(path)):
        pathcost+=getPathcost(graph, path[i-1], path[i])
    return pathcost

def astar(start, goal, previous=set(), currpath=[]):
    global minpc, minpath
    currpath.append(start)
    if start==goal:
        cost=totalPathcost(currpath)
        if cost<minpc:
            minpath = tuple(currpath)
            minpc=cost
        return
    nextset=list(set(graph[start][0])-previous)
    eval=[]
    for i in nextset:
        eval.append(graph[i][1]+getPathcost(graph, i, start))
    swapped = False
    for i in range(len(eval)-1):
        for j in range(0, len(eval)-i-1):
            if eval[j] > eval[j + 1]:
                swapped = True
                eval[j], eval[j + 1] = eval[j + 1], eval[j]
                nextset[j], nextset[j + 1] = nextset[j + 1], nextset[j]
        if not swapped:
            break
    for i in nextset:
        astar(i, goal, set(start), currpath)
        currpath.pop()
    return

astar('a', 'g')
print(minpath, minpc)
