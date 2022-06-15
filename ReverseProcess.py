import random
import heapq

def PartA(inputList):
    #print("")
    #print("Input List")
    #print(inputList)

    doubledList = []
    for i in inputList:
        doubledList.append(i*2)
    doubledList = doubledList + inputList
    random.shuffle(doubledList)
    return doubledList


def PartB(doubledList):
    #print("")
    #print("Doubled List")
    #print(doubledList)

    # Find Original List
    output = []
    doubles = set()
    heap = []
    heapq.heapify(heap)

    for i in doubledList:       # O(n)
        heapq.heappush(heap, i)   # O(log(n))

    #print("")
    #print("Heap:")
    #print(heap)

    while heap and len(output) < len(doubledList) // 2:           # O(n)
        num = heapq.heappop(heap)        # O(log(n))
        dubNum = num * 2
        if dubNum in doubles:
            doubles.remove(dubNum)         # O(1)
        else:
            doubles.add(num * 2)           # O(1)
            output.append(num)             # O(1)

    #print("")
    #print("Output List")
    #print(output)
    return output


# O(nlog(n))
for i in range(10):
    inputList = list(range(random.randint(0, 100), random.randint(100, 10000)))
    doubledList = PartA(inputList)
    originalInput = PartB(doubledList)
    print(originalInput == inputList)
