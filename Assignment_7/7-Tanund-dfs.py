#adjacency matrix

graph = [  # 1 2 3 4 5 6 7
            [0,1,0,0,0,0,0], # 1
            [0,0,0,1,0,0,1], # 2
            [0,0,0,1,0,0,0], # 3
            [0,0,0,0,0,1,0], # 4
            [0,0,1,1,0,0,0], # 5
            [0,0,0,0,0,0,0], # 6
            [0,0,0,0,1,0,0]  # 7
]
visited = list()

def DFS(graph, s):
    if s not in visited:
        print(s, "--->", end="")  #our answer
        visited.append(s)
        for idx, connect in enumerate(graph[s - 1]):  
            neighbor = idx + 1
            if neighbor not in visited and connect == 1:
                DFS(graph, neighbor)
              
                
DFS(graph, 1)