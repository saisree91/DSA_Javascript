def lcs_op(s1, s2, m, n, arr):
    if m == 0 or n == 0:
        return 0
    if arr[m][n] != -1:
        return arr[m][n]
    if s1[m-1] == s2[n-1]:
        arr[m][n] = 1 + lcs_op(s1, s2, m-1, n-1, arr)
        return arr[m][n]
    arr[m][n] = max(lcs_op(s1, s2, m-1, n, arr), lcs_op(s1, s2, m, n-1, arr))
    return arr[m][n]


def lcs(s1,s2):
    if(s1 > s2):
        s1, s2 = s2, s1
    print(s1)
    m = len(s1)
    n = len(s2)
    arr = [[-1 for i in range(n+1)] for i in range(m+1)]
    return lcs_op(s1, s2, m, n, arr)

s2 = "AGGTAB"
s1 = "GXTXAYB"
print(lcs(s1, s2))