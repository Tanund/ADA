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
def BFS(graph, s):
    visited = list()
    queue   = list()      #list in python is basically queue
    visited.append(s) #means make it black
    queue.append(s)
    
    while queue:      #as long as the queue is not empty....
        u = queue.pop(0)  #pop the front guy.....basically index 0
        
        print(u, "-->", end = "")
        
        for idx, connect in enumerate(graph[u - 1]):  
            neighbor = idx + 1
            if neighbor not in visited and connect == 1: #for everyone who connects to u,
                visited.append(neighbor)              #add them to the visited
                queue.append(neighbor)                #add them to the queue
                
BFS(graph, 1)