outputBFS = []
def traversalBFS(adjList):
    queue = [0]
    seen = set([])
    while queue:
        e = queue.pop(0)
        outputBFS.append(e)
        seen.add(e)
        for i in adjList[e]:
            if i not in seen:
                queue.append(i)

outputDFS = []
def traversalDFS(adjList, n=0):
    if n not in outputDFS:
        outputDFS.append(n)
        for i in adjList[n]:
            traversalDFS(adjList, i)

adjList = [[1,3],[0],[3,8],[0,4,5,2],[3,6],[3],[4,7],[6],[2]]
traversalBFS(adjList)
traversalDFS(adjList)
print(outputBFS)
print(outputBFS == [0, 1, 3, 4, 5, 2, 6, 8, 7])
print(outputDFS)
print(outputDFS == [0, 1, 3, 4, 6, 7, 5, 2, 8])
