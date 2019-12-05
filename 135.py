class Solution:
    def candy(self, ratings: List[int]) -> int:
        temp = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                temp[i] = temp[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                temp[i] = max(temp[i], temp[i + 1] + 1)
        return sum(temp)