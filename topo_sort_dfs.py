def topological_sort(V, Edges):
    adj_list = [[] for i in range(V)]
    print(adj_list)
    for u,v in Edges:
        adj_list[u].append(v)
    print(adj_list)
    visited = [0] * V
    stack = []
    def dfs(node):
        visited[node] = 1
        for adj_edge in adj_list[node]:
            if not visited[adj_edge]:
                dfs(adj_edge)
        stack.append(node)
    for i in range(V):
        if not visited[i]:
            dfs(i)
    return stack[::-1]

v = 6
edges = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
ans = topological_sort(v, edges)
print(ans)