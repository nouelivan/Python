# Rotates array A K times; that is, each element of A will be shifted to the right K times.

def solution(A, K):
    aCopy = A.copy()
    newInd = 0
    for n in range(len(A)):
        newInd = n + K
        if newInd < len(A):
            aCopy[newInd] = A[n]
        else:
            newInd = n + K
            while(newInd > len(A) - 1):
                newInd -= len(A)
            aCopy[newInd] = A[n]
    
    return aCopy
