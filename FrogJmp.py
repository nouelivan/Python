# Given three integers X, Y and D, this fucntion returns the minimal number of jumps a from must perform to get from position X to a position equal to or greater than Y.

def solution(X, Y, D):
    if X == Y:
        return 0
    elif (Y - X) % D == 0:
        return int((Y - X) / D)
    else:
        return int((Y - X) // D + 1)
    
