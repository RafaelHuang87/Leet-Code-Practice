class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        total = len(nums)
        if total <= 1:
            return False

        for i, v in enumerate(nums):
            head = i
            direction = v
            # print("====={}====".format(i))
            while True:
                step = nums[i]

                if step * direction < 0:  # wrong direction
                    break;

                next_i = (i + step) % total  # % always generate positive number
                if next_i == i:  # length-1 loop
                    break

                if next_i == head:
                    return True

                # fix step to point to head, so loop like 0 -> 1 ->2 ->1 can be detected when head is 0
                nums[i] = head - i + (total if direction > 0 else -total)  # keep direction correct
                # print("i={},next_i={},nums={}".format(i,next_i,nums))
                i = next_i
        return False