class TrieNode:
    """
    TrieNode represents a single node in the Trie data structure.
    """
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    """
    Trie is a tree-like data structure that stores a dynamic set of strings.
    """
    def __init__(self):
        self.root = TrieNode()

    # def print_trie(self):
    #     """
    #     Prints the entire Trie structure in a single line to get a visual idea of what it would look like
    #     """
    #     current_level = [("", self.root)]
    #     self._print_trie_recursive(current_level)

    # def _print_trie_recursive(self, current_level):
    #     """
    #     function for printing the Trie structure in a single line.
    #     """
    #     next_level = []
    #     for word, node in current_level:
    #         for char, child_node in node.children.items():
    #             new_word = word + char
    #             print(new_word, end=" ")
    #             next_level.append((new_word, child_node))

    #     if next_level:
    #         self._print_trie_recursive(next_level)
        
    def insert_word(self, word):
        """
        Inserts a word into the Trie.
        """
        # print(f"Inserting word: {word}")
        current_node = self.root
        for char in word: 
            if char not in current_node.children:
                # print(f"  Inserting character: {char}")
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        # print(f"  Marking {word} as a word")
        current_node.is_word = True

    def search_trie(self, word):
        """
        Searches for a word in the Trie, returning True if found and False otherwise.
        """
        # print(f"Searching for word: {word}")
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                print(f"  Word not found: {word}")
                return False
            current_node = current_node.children[char]
        # print(f"  Word found: {word}")
        return current_node.is_word

    def starts_with_prefix(self, prefix):
        """
        Checks if a given prefix exists in the Trie, returning True if found and False otherwise.
        """
        # print(f"Checking prefix: {prefix}")
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                # print(f"  Prefix not found: {prefix}")
                return False
            # print(f"  Traversing Trie for character: {char}")
            current_node = current_node.children[char]
        # print(f"  Prefix found: {prefix}")
        return True

# boggle_solver.py
class BoggleSolver:
    """
    BoggleSolver is a class for solving a Boggle game using a Trie data structure.
    """
    def __init__(self, trie, board):
        self.trie = trie
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.found_words = set()

    def solve_boggle(self):
        """
        Solves the Boggle game and returns a set of found words.
        """
        print("Solving Boggle")
        for row in range(self.rows):
            for col in range(self.cols):
                self.depth_field_search(row, col, "")
        return self.found_words

    def depth_field_search(self, row, col, current_word):
        """
        Depth-first search helper function to explore possible words in the Boggle board.
        """
        # print(f"Explorer at ({row}, {col}), Current word: {current_word}")
        # print("Visited cells:")
        # for visited_row in self.visited:
        #     print(" ".join("X" if visited else "." for visited in visited_row))
        # print("\n")
        
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.visited[row][col]:
            return

        current_word += self.board[row][col]
        if not self.trie.starts_with_prefix(current_word):
            return

        if self.trie.search_trie(current_word):
            self.found_words.add(current_word)
        if self.trie.search_trie(current_word):
            print(f"  Found word: {current_word}")
            self.found_words.add(current_word)

        self.visited[row][col] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            self.depth_field_search(row + dr, col + dc, current_word)

        self.visited[row][col] = False

if __name__ == "__main__":
    def load_dictionary(file_path):
        """
        Loads a dictionary from a text file, with one word per line, and inserts the words into a Trie.
        """
        trie = Trie()
        with open(file_path, 'r') as file:
            for word in file:
                trie.insert_word(word.strip())
        return trie

    dictionary_file_path = './signature.txt'
    trie = load_dictionary(dictionary_file_path)
    # trie.print_trie()

    board = [
        ['b', 'e', 'a', 'r'],
        ['o', 'u', 'l', 'l'],
        ['n', 'c', 'z', 'e'],
        ['e', 'f', 't', 'b']
    ]

    boggle_solver = BoggleSolver(trie, board)
    found_words = boggle_solver.solve_boggle()

    print("Found words:")
    for word in found_words:
        print(word)

    print("Total number of words found:", len(found_words))
