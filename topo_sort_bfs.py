def topological_sort(V, Edges):
    adj_list = [[] for i in range(V)]
    indegree = [0] * V
    for u,v in Edges:
        adj_list[u].append(v)
        indegree[v] += 1
    queue = [i for i in range(V) if indegree[i] == 0]
    ordered_topo = []
    while queue:
        node = queue.pop(0)
        ordered_topo.append(node)
        for adj_edge in adj_list[node]:
            indegree[adj_edge] -= 1
            if indegree[adj_edge] == 0:
                queue.append(adj_edge)
    if len(ordered_topo) == V:
        return ordered_topo

vertices = 6
edges = [[5, 0], [5, 2], [4, 0], [4, 1], [2, 3], [3, 1]]
ans = topological_sort(vertices, edges)
print(ans)