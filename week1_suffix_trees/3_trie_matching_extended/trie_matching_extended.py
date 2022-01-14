# python3
import sys

NA = -1


def build_trie_with_end(patterns):
    tree = {0: {}}
    node = 0
    for pattern in patterns:
        i = 0
        for letter in pattern[:-1]:
            if letter in tree[i]:
                i = tree[i][letter][0]
            else:
                node += 1
                tree[i][letter] = (node, 0)
                tree[node] = {}
                i = node

        l = pattern[-1]
        if l in tree[i]:
            tree[i][l] = (node, 1)
        else:
            node += 1
            tree[i][l] = (node, 1)
            tree[node] = {}
    return tree


def solve(text, patterns):
    trie = build_trie_with_end(patterns)
    result = []
    for i in range(len(text)):
        node = 0
        for j in range(i, len(text)):
            if text[j] in trie[node]:
                if trie[node][text[j]][1] == 1:
                    result.append(i)
                    break
                node = trie[node][text[j]][0]
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
