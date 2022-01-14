# python3
import sys


def build_trie(patterns):
    tree = {0: {}}
    nodes = {}
    node = 0
    to_add = -1
    for pattern in patterns:
        i = 0
        to_add += 1
        for l in range(len(pattern)):
            if pattern[l] in tree[i]:
                i = tree[i][pattern[l]]
            else:
                node += 1
                tree[i][pattern[l]] = node
                nodes[node] = [i, to_add + l, to_add + l]  # (parent, start, finish)
                tree[node] = {}
                i = node
    return tree, nodes


def compress_trie(trie, nodes):
    dollar_nodes = []
    for key in nodes:
        if not trie[key]:
            dollar_nodes.append(key)

    for key in dollar_nodes:
        while key != 0:
            parent = nodes[key][0]
            if len(trie[parent]) == 1:
                nodes[key][1] = nodes[parent][1]
                nodes[key][0] = nodes[parent][0]
                del nodes[parent]
            else:
                key = parent  #new parent
    return nodes


def build_suffix_tree(text):
    patterns = [text[i:] for i in range(len(text))]
    result = []
    trie, nodes = build_trie(patterns)
    nodes = compress_trie(trie, nodes)
    for key in nodes:
        print(text[nodes[key][1]:nodes[key][2] + 1])
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)

"""
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
