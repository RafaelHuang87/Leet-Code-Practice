class Solution:
    def findWords(self, words: [str]) -> [str]:
        chars_in_row = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ret = []

        for word in words:
            row = 0

            if word[0].lower() in chars_in_row[1]:
                row = 1
            elif word[0].lower() in chars_in_row[2]:
                row = 2
            else:
                None

            word_len = len(word)
            take_word = True

            for a in range(1, word_len):
                if word[a].lower() not in chars_in_row[row]:
                    take_word = False

            if take_word:
                ret.append(word)

        return ret
s = ''
for i in range(200):
    if i == 0:
        s += 'o'
    else:
        s += 'a'
print([s])
print(Solution().findWords([s]))