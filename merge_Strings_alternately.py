class solution():
    def mergeAlternately(self, word1: str, word2: str) -> str:
        array_solution = [0] * (len(word1) + len(word2))
        # same length of words
        if len(word1) == len(word2):
            for i,n in enumerate(word1):
                array_solution[i] = n
                i += 1

        return array_solution

x = solution()

print(x.mergeAlternately('xxx','zzz'))

