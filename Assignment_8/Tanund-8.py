from operator import truediv
from heapdict import heapdict

def find_weight(G, u, v):
    for i in G[u]:
        if v == i[0]:
            return i[1]
    return None

def adj(G, u):
    neighbors = []
    for _, val in enumerate(G[u]):
        neighbors.append(val[0])
    return neighbors

def check_v_in_Q(Q, v):
    keys = list(Q.keys())
    if v in keys:
        return True
    return False

# use tuple to store adjacent vertex and weight (V,W)
G = {
    0: [(1,2),(2,2),(3,5),(4,3)],
    1: [(0,2),(2,1),(3,4),(4,4)],
    2: [(0,2),(1,1),(3,3),(4,5)],
    3: [(0,5),(1,4),(2,3),(4,9)],
    4: [(0,3),(1,4),(2,5),(3,9)]
}
#     #0 1 2 3 4
# G = [
#     [0,2,2,5,3], # 0
#     [2,0,1,4,4], # 1
#     [2,1,0,3,5], # 2
#     [5,4,3,0,9], # 3
#     [3,4,5,9,0], # 4
# ]

INF = 9999
N = 5
r = 0

# for each vertex
# set key to inf
# put all vertex into queue
Q = heapdict()
for i in range(N):
    Q[i] = INF
# r.key = 0 
Q[r] = 0

print(f"Queue: {list(Q.items())}")

# set pi to NIL
pi = [None] * 5

# set pi of r = -1 or anything you like
pi[r] = -1



# while q is not empty
while Q:
    # u = extract min
    u = Q.popitem()[0]
    # for v in adj[u]
    for v in adj(G, u):
        
        # if v in Q, and w(u, v) < v.key
        if check_v_in_Q(Q, v) and find_weight(G, u, v) < Q[v]:
            # v.pi = u
            pi[v] = u
            # v.key = w(u, v)
            Q[v] = find_weight(G, u, v)


print(f"PI: {pi}")

w = 0
for i in range(len(pi)):
    if pi[i] != -1:
        w = w + find_weight(G, i, pi[i])

print('weight: ' + str(w))
