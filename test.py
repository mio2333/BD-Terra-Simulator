import numpy as np

up_probs = [0.5,0.45,0.4,0.35,0.3,0.25]
def P(i,j):
    if abs(i-j)>1: return 0
    if j>i: return up_probs[i]
    if j==i:
        if i==0 or i==5:
            return up_probs[i]
        else:
            return 0
    if j<i:
        return 1-up_probs[i]

def gen_mat(end):
    b = [[-1],[-1],[-1],[-1],[-1],[-1]]
    b[end] = [0]
    A = []
    for i in range(6):
        if i==end:
            t = [0 for j in range(6)]
            t[end] = 1
        else:  
            t = [P(i,j) for j in range(6)]
            t[i] -= 1
        A.append(t)
    return A,b

def one_skill_distance(a,b):
    if a==b: return 0
    A,b = gen_mat(b)
    A = np.array(A)
    b = np.array(b)
    sol = np.linalg.solve(A, b)
    return sol[a]

def foul_skill_distance(alist,blist):
    s = 0
    for a,b in zip(alist,blist):
        if b>a: s+= one_skill_distance(a,b)
    return s

print(foul_skill_distance([0,0,0,0],[5,5,5,5]))