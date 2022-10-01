# Finds the value in a list that occurs an odd number of times.

def solution(A):
    A.sort()

    while(True):
        if A.count(A[0]) % 2 == 0:
            del A[:A.count(A[0])]
        else:
            return A[0]
          
          
