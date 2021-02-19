class Recursion:
    def find_contain_word(self, word, word_dict):
        len_word = len(word)
        if len_word < 1:
            print("Invalid String")
            return
        self._find_contain_word(word, word_dict, [])

    def _find_contain_word(self, word, word_dict, gen_word):
        if len(word) == 0:
            print (gen_word)
            return

        for i in range(0, len(word)):
            cur_word = word[:i + 1]
            if cur_word in word_dict:
                gen_word.append(cur_word)
                self._find_contain_word(word[i + 1:], word_dict, gen_word)
                gen_word.pop()


if __name__ == '__main__':
    a = Recursion()
    (a.find_contain_word("catsanddog", ["cat", "cats", "sand", "and", "dog"]))
