from operator import truediv
from heapdict import heapdict

# implement Dijkstra algorithm

def adj(G, u):
    neighbors = []
    for idx, _ in enumerate(G[u]):
        if G[u][idx] != 0:
            neighbors.append(idx)
    return neighbors

def check_v_in_Q(Q, v):
    keys = list(Q.keys())
    if v in keys:
        return True
    return False

INF = 9999
    #0   1   2   3   4   5   6   7   8
G = [
    [0  ,4  ,INF,INF,INF,INF,INF,8  ,INF], # 0
    [4  ,0  ,8  ,INF,INF,INF,INF,11 ,INF], # 1
    [INF,8  ,0  ,7  ,INF,4  ,INF,INF,2  ], # 2
    [INF,INF,7  ,0  ,9  ,14 ,INF,INF,INF], # 3
    [INF,INF,INF,9  ,0  ,10 ,INF,INF,INF], # 4
    [INF,INF,4  ,14 ,10 ,0  ,2  ,INF,INF], # 5
    [INF,INF,INF,INF,INF,2  ,0  ,1  ,6  ], # 6
    [8  ,11 ,INF,INF,INF,INF,1  ,0  ,7  ], # 7
    [INF,INF,2  ,INF,INF,INF,6  ,7  ,0  ], # 8
]

N = 9
r = 0

# for each vertex
# set key to inf
# put all vertex into queue
Q = heapdict()
for i in range(N):
    Q[i] = INF
# r.key = 0 
Q[r] = 0

# print(f"Queue: {list(Q.items())}")

# set pi to NIL
pi = [None] * N

# set pi of r = -1 or anything you like
pi[r] = -1

# while q is not empty
while Q:
    # u = extract min
    popped_item = Q.popitem()
    u = popped_item[0]
    u_key = popped_item[1]
    # for v in adj[u]
    for v in adj(G, u):
        
        # if v in Q, and w(u, v) + u.key < v.key
        if check_v_in_Q(Q, v) and G[u][v] + u_key < Q[v]:
            # v.pi = u
            pi[v] = u
            # v.key = w(u, v) + u.key
            Q[v] = G[u][v] + u_key

print(f"PI: {pi}")
w = 0
for i in range(len(pi)):
    if pi[i] != -1:
        w = w + G[i][pi[i]]

# print('weight: ' + str(w))