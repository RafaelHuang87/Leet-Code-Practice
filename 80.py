class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if(len(nums)<=2):return len(nums)
        i=2
        a=2
        while(i<len(nums)):
            if nums[i]!=nums[a-2]:
                nums[a]=nums[i]
                a=a+1
            i=i+1
        return a