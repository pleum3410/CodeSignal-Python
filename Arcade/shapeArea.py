# n = 1 2 3 4 5
# poly,p = 1  5  13  25   41   
# diff,d1 =  4  8   12  16
# diff2,d2 =  4  4    4
# n > func > poly
# func = max(∀{x∈N,0<x<n},px=(p(x-1))+(d2*x-1))

def solution(n):
    p = [1]*(n+1) #p = polygon numbers
    for x in range(1, n+1):
        p[x] = p[x-1]+(4*(x-1))
    return max(p)
