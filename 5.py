
class Solution:
    def longestPalindrome(s):
        mx = 0
        ans = 0
        po = 0
        Len = [0] * 10000

        def transform(s):
            init_s = '@#'
            for x in s:
                init_s = init_s + x + '#'

            return init_s + '$', 2 * len(s) + 1

        init_s, len_s = transform(s)
        get_po = 0
        for i in range(1, len_s):
            if mx > i:
                Len[i] = min(mx - i, Len[2 * po - i])
            else:
                Len[i] = 1

            while init_s[i - Len[i]] == init_s[i + Len[i]]:
                Len[i] = Len[i] + 1

            if Len[i] + i > mx:
                mx = Len[i] + i
                po = i


            if ans < Len[i]:
                ans = Len[i]
                get_po = i


        return init_s[get_po-ans + 2: get_po + ans: 2]