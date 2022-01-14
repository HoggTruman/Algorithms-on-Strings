# python3
import sys

def BWT(text):
    ans = ""
    n = len(text)
    holder = []
    for i in range(n):
        holder.append(text[i:] + text[:i])
    holder.sort()
    for i in range(n):
        ans += holder[i][n-1]

    return ans

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))