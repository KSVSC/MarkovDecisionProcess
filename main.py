#Value iteration
import sys
from copy import deepcopy

def move_possible(i, j):
    #out of the boundary
    if i < 0 or j < 0 or i >= n or j >= m:
        return False
    #check if wall
    if [i, j] in W:
        return False
    return True
    
def Prob_utility(i, j):
    maxVal = float("-inf")

    val = 0
    if (move_possible(i + 1, j)):
        val += 0.8 * U[i + 1][j]
    else:
        val += 0.8 * U[i][j]
    if (move_possible(i, j - 1)):
        val += 0.1 * U[i][j - 1]
    else:
        val += 0.1 * U[i][j]
    if (move_possible(i, j + 1)):
        val += 0.1 * U[i][j + 1]
    else:
        val += 0.1 * U[i][j]
    # val += S
    if (val > maxVal):
        maxVal = val
        P[i][j] = 'S'


    val = 0
    if (move_possible(i, j + 1)):
        val += 0.8 * U[i][j+1]
    else:
        val += 0.8 * U[i][j]
    if (move_possible(i + 1, j)):
        val += 0.1 * U[i + 1][j]
    else:
        val += 0.1 * U[i][j]
    if (move_possible(i - 1, j)):
        val += 0.1 * U[i - 1][j]
    else:
        val += 0.1 * U[i][j]
    # val += S
    if (val > maxVal):
        maxVal = val
        P[i][j]='E'

    val = 0
    if (move_possible(i - 1, j)):
        val += 0.8 * U[i -1][j]
    else:
        val += 0.8 * U[i][j]
    if (move_possible(i, j + 1)):
        val += 0.1 * U[i][j + 1]
    else:
        val += 0.1 * U[i][j]
    if (move_possible(i, j - 1)):
        val += 0.1 * U[i][j - 1]
    else:
        val += 0.1 * U[i][j]
    # val += S
    if (val > maxVal):
        maxVal = val
        P[i][j]='N'

    val = 0
    if (move_possible(i, j - 1)):
        val += 0.8 * U[i][j - 1]
    else:
        val += 0.8 * U[i][j]
    if (move_possible(i + 1, j)):
        val += 0.1 * U[i + 1][j]
    else:
        val += 0.1 * U[i][j]
    if (move_possible(i - 1, j)):
        val += 0.1 * U[i - 1][j]
    else:
        val += 0.1 * U[i][j]
    # val += S
    if (val > maxVal):
        maxVal = val
        P[i][j]='W'

    return maxVal
        

if __name__ == '__main__':
    # size of grid
    L1 = [int(i) for i in input().split()]
    n = L1[0]
    m = L1[1]

    #reward for each state
    R = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        L2 = [float(k) for k in input().split()]
        for j in range(m):
            R[i][j] = L2[j]

    # noof exit states and walls
    L3 = [int(i) for i in input().split()]
    e = L3[0]
    w = L3[1]

    #coord of exit states
    E = [[0 for i in range (2)] for j in range (e)]
    for i in range(e):
        E[i] = [int(j) for j in input().split()]

    #coord of wall
    W = [[0 for i in range(2)] for j in range(w)]
    for i in range(w):
        W[i] = [int(j) for j in input().split()]

    #coord of start state
    L4 = [int(i) for i in input().split()]

    # unit step reward
    S = float(input())

    temp_U = [[0 for i in range(m)] for j in range(n)]
    U = [[0 for i in range(m)] for j in range(n)]
    P = [[0 for i in range(m)] for j in range(n)]

    dis_fac = 0.99

    z = 0
    while True:
        z += 1
        delta = 0
        U = deepcopy(temp_U)

        for i in range(n):
            for j in range(m):
                if [i, j] in E:
                    temp_U[i][j] = R[i][j]
                    P[i][j] = R[i][j]
                elif [i, j] in W:
                    temp_U[i][j] = 0
                    P[i][j] = '-'
                else:
                    temp_U[i][j] = R[i][j] + S + dis_fac * Prob_utility(i, j)
                delta = max(delta, abs(temp_U[i][j] - U[i][j]))

        print("iteration", z, "delta", delta)
        print("utility")
        for i in range(n):
            for j in range(m):
                print(round(temp_U[i][j],3),end=' ')
            print()
        print("\n")

        if delta < 0.01*(1-dis_fac)/dis_fac:
            break
    print("policy:")
    for i in range(n):
        for j in range(m):
            print(P[i][j],end=' ')
        print()

        
            




    
