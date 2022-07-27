from collections import defaultdict


class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.
    """

    def __init__(self):
        self.root = defaultdict()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word: str):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word: str):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix: str):
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True

    def __repr__(self):
        def recur(node, indent):
            if not node:
                return ""
            return "".join(
                indent +
                key +
                recur(child, indent + "  ")
                for key, child in node.items()
            )

        return recur(self.root, "\n")


def create_trie(words: list[str]):
    head = Trie()
    for word in words:
        head.insert(word)
    return head


trie = create_trie(["ciao", "ciaoo", "ciaopp", "bai"])
print(trie)

print("\"ci\" in trie:", trie.search("ci"))
print("\"ciao\" in trie:", trie.search("ciao"))
print("\"ciaoo\" in trie:", trie.search("ciaoo"))
print("\"ciaop\" in trie:", trie.search("ciaop"))
print("\"cia\" in trie:", trie.search("cia"))
print("\"bai\" in trie:", trie.search("bai"))

trie.insert("ci")
print(trie)
print("\"ci\" in trie:", trie.search("ci"))
