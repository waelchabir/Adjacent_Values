ADJECENT_NOT_FOUND = -1
MAX_LIST_LENGTH = 40000

def getDistance(x, y):
    distance = x - y
    if (distance >= 0):
        return int(distance)
    return (-1) * int(distance)

def getClosestAdjacent(A, startIndice):
    nextIndice = startIndice + 1
    adjacentList = []
    for i in range(nextIndice, len(A)):
        if (A[startIndice] != A[i]):
            isAdjacent = True
            for j in range(len(A)):
                if A[startIndice] < A[i]:
                    if ((A[startIndice] < A[j] < A[i]) and (A[startIndice] != A[j])) and (j != i) and (j != startIndice):
                        isAdjacent = False
                if ((A[startIndice] > A[j] > A[i]) and (A[startIndice] != A[j])) and (j != i) and (j != startIndice):
                        isAdjacent = False
            if isAdjacent:
                adjacentList.append(str(startIndice) + ',' + str(i) + ',' + str(getDistance(startIndice, i)))
    return adjacentList

def getLeastDistance(L):
    minDistance = MAX_LIST_LENGTH
    for i in range(len(L)):
        distance = L[i].split(',')[2]
        if(int(distance) < int(minDistance)):
            minDistance = distance
    return minDistance

def solution(A):
    # write your code in Python 3.6
    if len(A) > MAX_LIST_LENGTH:
        return ADJECENT_NOT_FOUND
    adjacents = []
    for i in range(len(A)):
        result = getClosestAdjacent(A, i)
        if len(result) > 0:
            for element in result:
                adjacents.append(element)
    if(len(adjacents) == 0):
        return ADJECENT_NOT_FOUND
    leastDistance = getLeastDistance(adjacents)
    return leastDistance

if __name__ == "__main__":
    # list = [0, 3, 3, 7, 5, 3, 11, 1]
    list = [1, 4, 7, 3, 3, 5]
    result = solution(list)
    print(result)