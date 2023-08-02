def lcs_algo(S1, S2):
    m = len(S1)
    n = len(S2)
    
    # Create a matrix to memoize the results of subproblems
    L = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # Following the backtrack from the bottom-right to the top-left corner of the matrix
    lcs = []
    i = m
    j = n
    while i > 0 and j > 0:
        if S1[i-1] == S2[j-1]:
            lcs.insert(0, S1[i-1])
            i -= 1
            j -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    # Print the sub sequences
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs))


S1 = "ACADB"
S2 = "CBDA"
lcs_algo(S1, S2)
