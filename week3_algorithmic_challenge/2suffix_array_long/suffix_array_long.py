# python3
import sys

def CharI(x):
    if x == "A":
        return 1
    if x == "C":
        return 2
    if x == "G":
        return 3
    if x == "T":
        return 4
    return 0

def SortCharacters(S):
    order = [0]*len(S)
    count = [0]*5                ## $ACGT
    for i in range(len(S)):
        count[CharI(S[i])] = count[CharI(S[i])] + 1
    for j in range(1, 5):
        count[j] += count[j-1]
    for i in range(len(S)-1, -1, -1):
        c = CharI(S[i])
        count[c] -= 1
        order[count[c]] = i
    return order


def ComputeCharClasses(S,order):
    classes = [0]*len(S)
    classes[order[0]] = 0
    for i in range(1, len(S)):
        if S[order[i]] != S[order[i-1]]:
            classes[order[i]] = classes[order[i-1]] + 1
        else:
            classes[order[i]] = classes[order[i-1]]
    return classes


def SortDoubled(S, L, order, classes):
    count = [0]*len(S)
    new_order = [0]*len(S)
    for i in range(len(S)):
        count[classes[i]] = count[classes[i]] + 1
    for j in range(1, len(S)):
        count[j] += count[j-1]
    for i in range(len(S)-1, -1, -1):
        start = (order[i] - L + len(S)) % len(S)
        cl = classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order

def UpdateClasses(order, classes, L):
    n = len(order)
    newClass = [0]*n
    newClass[order[0]] = 0
    for i in range(1, n):
        cur, prev = order[i], order[i-1]
        mid, midPrev = (cur+L) % n, (prev+L) % n
        if classes[cur] != classes[prev] or classes[mid] != classes[midPrev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]

    return newClass


def build_suffix_array(S):
    order = SortCharacters(S)
    classes = ComputeCharClasses(S, order)
    L = 1
    while L < len(S):
        order = SortDoubled(S, L, order, classes)
        classes = UpdateClasses(order, classes, L)
        L = 2*L

    return order


def build_suffix_array_naive(text):  #memory issues but not too slow
    store = [0] * len(text)
    for i in range(len(text)):
        store[i] = (text[i:], i)
    store.sort()

    result = []
    for i in range(len(text)):
        result.append(store[i][1])

    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
