class Recursion:
    def anagrams(self, word):
        len_word = len(word)
        if len_word < 2:
            print(word)
            return
        used = [False] * len_word
        self.__anagram(word, list(word), used, 0)

    def __anagram(self, word, comb, used, start):
        word_len = len(word)
        if start == word_len:
            print("".join(comb))
            return

        for x in range(0, word_len):
            if not used[x]:
                used[x] = True
                comb[start] = word[x]
                self.__anagram(word, comb, used, start + 1)
                used[x] = False


if __name__ == '__main__':
    a = Recursion()
    a.anagrams("xda")
