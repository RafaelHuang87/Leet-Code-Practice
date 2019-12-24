class Solution:
    def countBits(self, num: int) -> List[int]:
        templist = [0]
        while (len(templist) <= num):
            templist2 = [i + 1 for i in templist]
            templist = templist + templist2

        return templist[:num + 1]