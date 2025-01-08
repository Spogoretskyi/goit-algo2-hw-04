from base_trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        common_prefix = strings[0]

        for word in strings[1:]:
            new_common_prefix = []
            for i in range(min(len(common_prefix), len(word))):
                if common_prefix[i] == word[i]:
                    new_common_prefix.append(common_prefix[i])
                else:
                    break

            common_prefix = "".join(new_common_prefix)

            if not common_prefix:
                break

        return common_prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    
    # Тест 1
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    # Тест 2
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    # Тест 3
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
