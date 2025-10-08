def dfs_count(graph, visited):
    network = [[],[]]
    network_index = 0
    stack = []
    for i in range(1, len(graph)):
        if not visited[i]:
            visited[i] = True
            stack.append(graph[i])
            network[network_index].append(i)
            while stack:
                node = stack.pop()
                for v in node:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(graph[v])
                        network[network_index].append(v)
            network_index = 1

    #print(network)
            
    return abs(len(network[0]) - len(network[1]))

def solution(n, wires):
    
    differences = []
    
    for i in range(len(wires)):
        convert = [[] for _ in range(n+1)]
        visited = [False]*(n+1)
        wires_case = [v for v in wires if wires.index(v) != i]
        
        #print(wires_case)
        
        for j, k in wires_case:
            convert[k].append(j)
            convert[j].append(k)
        
        #print(convert)
        differences.append(dfs_count(convert, visited))
    
    return min(differences)