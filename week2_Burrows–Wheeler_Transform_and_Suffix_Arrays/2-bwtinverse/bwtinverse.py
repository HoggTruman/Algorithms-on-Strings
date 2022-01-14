# python3
import sys

def InverseBWT(bwt):
    n = len(bwt)
    B = [bwt[i] for i in range(n)]

    for i in range(n-1):
        B.sort()
        for i in range(n):
            B[i] = bwt[i] + B[i]

    for i in range(n):
        if B[i][n-1] == "$":
            return B[i]

def InverseBWTCOoL(text):
    n = len(text)
    textaslist = [t for t in text]
    t = [i for i in range(len(text))]
    s_t = sorted(t, key=dict(zip(t, textaslist)).get)

    ans = ""
    i = 0
    for iter in range(n):
        ans = text[s_t[i]] + ans
        i = s_t.index(t[i])

    return ans

def InverseBWTCOooLer(text):
    n = len(text)
    textaslist = [t for t in text]
    numlist = [i for i in range(n)]



    s_t = sorted(numlist, key=dict(zip(numlist, textaslist)).get)
    bwt = {s_t[i]: i for i in range(n)}  # will give index of character i in the sorted one
    inv_bwt = {bwt[i]: i for i in bwt}


    ans = ""
    i = 0
    for iter in range(n):
        ans = ans + text[inv_bwt[i]]
        i = s_t[i]

    return ans[1:] + ans[0]

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWTCOooLer(bwt))