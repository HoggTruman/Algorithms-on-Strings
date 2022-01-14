# python3
import sys

NA = -1

def build_trie(patterns):
    tree = {0: {}}
    node = 0
    for pattern in patterns:
        i = 0
        for letter in pattern:
            if letter in tree[i]:
                i = tree[i][letter]
            else:
                node += 1
                tree[i][letter] = node
                tree[node] = {}
                i = node
    return tree


def solve(text, patterns):
    trie = build_trie(patterns)
    print(trie)
    result = []
    for i in range(len(text)):
        node = 0
        for j in range(i, len(text)):
            if text[j] in trie[node]:
                node = trie[node][text[j]]
                if trie[node] == {}:
                    result.append(i)
                continue
            break

    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
