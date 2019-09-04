"""
Solution for Leet Code 804.
"""
from _ast import List


class Solution:
    def uniqueMorseRepresentations(words) -> int:
        list_mose = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        list_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

        dictionary = dict(zip(list_char, list_mose))

        result = []
        i = 0
        for word in words:
            tmp = ''
            for char in word:
                tmp = tmp + dictionary[char]
            if tmp not in result:
                result.append(tmp)
                i += 1
        return i

print(Solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))