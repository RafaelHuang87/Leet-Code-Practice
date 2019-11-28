class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        heights.append(0)
        i = 0
        max_m = 0
        stack = []
        while i < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i = i + 1
            else:

                while stack != [] and heights[stack[-1]] > heights[i]:
                    a = stack.pop()
                    if stack == []:
                        max_m = max(max_m, i * heights[a])
                    else:
                        max_m = max(max_m, (i - stack[-1] - 1) * heights[a])

        return max_m

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
