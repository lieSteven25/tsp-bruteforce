from itertools import permutations

dist = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

n = len(dist)
cities = list(range(1, n))

min_cost = float('inf')
best_route = []

for p in permutations(cities):
    cost = 0
    k = 0
    for city in p:
        cost += dist[k][city]
        k = city
    cost += dist[k][0]

    if cost < min_cost:
        min_cost = cost
        best_route = p

print("Minimum Cost:", min_cost)
print("Route: 0 ->", " -> ".join(map(str, best_route)), "-> 0")
