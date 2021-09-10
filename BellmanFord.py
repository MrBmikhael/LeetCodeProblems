times = [[1,4,2], [1,2,9], [4,2,-4], [2,5,-3], [4,5,6], [5,3,7], [3,2,3], [3,1,5]]
n = 5
k = 1

def bellmanFord():
    distances = [float('inf')] * n
    distances[k-1] = 0
    
    for i in range(n-1):
        for j in range(len(times)):
            src = times[j][0]
            dst = times[j][1]
            weight = times[j][2]
            distances[dst-1] = min(distances[dst-1], distances[src-1] + weight)

    return distances

def negativeCycle(distancesArr):
    distances = distancesArr[:]
    for j in range(len(times)):
        src = times[j][0]
        dst = times[j][1]
        weight = times[j][2]
        if distances[dst-1] > distances[src-1] + weight:
            return True
    return False

distances = bellmanFord()
print(distances)
negativeCycleDetected = negativeCycle(distances)
print(negativeCycleDetected)
