# Design-6

## Problem1 Design Phone Directory (https://leetcode.com/problems/design-phone-directory/) - Leetcode premium

class PhoneDirectory:
    def __init__(self, max_numbers: int):
        """
        Initialize the phone directory.
        @param max_numbers: The maximum numbers that can be stored in the phone directory.
        """
        self.is_provided = [False] * max_numbers  # List to track availability of numbers.

    def get(self) -> int:
        """
        Provide a number that is not assigned to anyone.
        @return: Return an available number. Return -1 if none is available.
        """
        for i, available in enumerate(self.is_provided):
            if not available:  # If the number is available
                self.is_provided[i] = True  # Mark the number as taken
                return i  # Return the number
        return -1  # Return -1 if no numbers are available

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        @param number: The number to be checked.
        @return: True if the number is available, False otherwise.
        """
        return not self.is_provided[number]  # Return the negation of the provided status of the number

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        @param number: The number to be released.
        """
        self.is_provided[number] = False  # Mark the number as available again

'''
1. init: TC = O(n)
2. get:  TC = O(n) 
3. check: TC = O(1)
4. release: TC = O(1)
4. SC = O(n)
'''


## Problem2 Design Autocomplete System (https://leetcode.com/problems/design-search-autocomplete-system/) - Leetcode premium

class TrieNode:
    def __init__(self):
        # Initialize 27 children for each letter in the alphabet plus the space character
        self.children = [None] * 27
        self.value = 0  # Frequency of word ending at this node
        self.word = ''  # The word ending at this node, if any

    def insert(self, word, frequency):
        # Inserts a word into the trie along with its frequency
        node = self
        for char in word:
            index = 26 if char == ' ' else ord(char) - ord('a')  # Mapping 'a'-'z' to 0-25, ' ' to 26
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.value += frequency
        node.word = word

    def search(self, prefix):
        # Searches for a node in the trie that corresponds to the given prefix
        node = self
        for char in prefix:
            index = 26 if char == ' ' else ord(char) - ord('a')
            if node.children[index] is None:
                return None
            node = node.children[index]
        return node

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = TrieNode()
        for sentence, frequency in zip(sentences, times):
            self.trie.insert(sentence, frequency)
        self.typed_characters = []  # Keeps track of characters typed by the user

    def input(self, character):
        # Returns autocomplete suggestions based on the characters inputted so far

        def dfs(node):
            # Perform a depth-first search to find all words with their frequencies
            if node is None:
                return
            if node.value:
                results.append((node.value, node.word))
            for next_node in node.children:
                dfs(next_node)

        if character == '#':
            # The user finished typing a word; update the trie and reset the input
            current_sentence = ''.join(self.typed_characters)
            self.trie.insert(current_sentence, 1)  # Increment the frequency of the word
            self.typed_characters = []
            return []

        results = []
        self.typed_characters.append(character)
        current_prefix = ''.join(self.typed_characters)
        node = self.trie.search(current_prefix)
        # If the prefix doesn't exist in the trie, return an empty list
        if node is None:
            return []
        # Otherwise, find and return autocomplete suggestions
        dfs(node)
        # Sort the results in descending order of frequency, and alphabetically for ties
        results.sort(key=lambda x: (-x[0], x[1]))
        # Return the top 3 suggestions, or fewer if there aren't enough
        return [entry[1] for entry in results[:3]]
    
'''
1. Insert: TC = O(n), SC = O(n)
2. search:  TC = O(m), SC = O(n) 
3. input: TC = O(m + p + q * k + x * log(x)), SC = O(q * k)
'''