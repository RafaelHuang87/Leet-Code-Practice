class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        times = minutesToTest / minutesToDie + 1  # 每头猪最多可测试的水桶数
        num = 0
        while pow(times, num) < buckets:
            num = num + 1
        return num
