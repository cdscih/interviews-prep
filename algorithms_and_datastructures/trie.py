class TrieNode:
    def __init__(self):
        self.paths = {}
        self.is_word = False

    def __str__(self):
        # TODO: fix the addition case
        tpl = ""
        stack = [self]
        while stack:
            node = stack.pop()
            for char, node in node.paths.items():
                tpl += f" ({char}) "
                stack.append(node)
        return tpl


def add_to_trie(head: TrieNode, word: str):
    cur = head
    for char in word:
        if char not in cur.paths:
            cur.paths[char] = TrieNode()
        cur = cur.paths[char]
    cur.is_word = True


def create_trie(words: list[str]):
    head = TrieNode()
    for word in words:
        add_to_trie(head, word)
    return head


def in_trie(head: TrieNode, word: str):
    trie_cur = head
    for i, _ in enumerate(word):
        if word[i] not in trie_cur.paths:
            return False
        trie_cur = trie_cur.paths[word[i]]
    return trie_cur.is_word


trie = create_trie(["ciao", "ciaoo", "ciaopp", "bai"])
print(trie)

print("\"ci\" in trie:", in_trie(trie, "ci"))
print("\"ciao\" in trie:", in_trie(trie, "ciao"))
print("\"ciaoo\" in trie:", in_trie(trie, "ciaoo"))
print("\"ciaop\" in trie:", in_trie(trie, "ciaop"))
print("\"cia\" in trie:", in_trie(trie, "cia"))
print("\"bai\" in trie:", in_trie(trie, "bai"))

add_to_trie(trie, "ci")
print("\"ci\" in trie:", in_trie(trie, "ci"))

print(trie)
