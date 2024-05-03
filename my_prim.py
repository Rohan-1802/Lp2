import heapq
def prim(graph):
    visited=[]
    mst=[]
    pq=[(0,None,next(iter(graph)))]
    while pq:
        weight,u,v=heapq.heappop(pq)
        if v not in visited:
            mst.append((u,v,weight))
            visited.append(v)
            for n,w in graph[v]:
                if n not in visited:
                    heapq.heappush(pq,(w,v,n))
    return mst

graph = {

    'A': [('B', 4), ('C', 3)], 'B': [('A', 2), ('C', 1), ('D', 1)],
'C': [('A', 3), ('B', 4), ('D', 1)], 'D': [('B', 1), ('C', 4)]

    }


ans=prim(graph)
print(ans)
