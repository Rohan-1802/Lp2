graph={
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def dfs(node,visited,graph):
    if node not in visited:
        visited.append(node)
        for k in  graph[node]:
            dfs(k,visited,graph)
    return visited

visited =[]
dfs('A',visited,graph)
print(visited)


