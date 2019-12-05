class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            if i - 1 >= 0 and gas[i - 1] > cost[i - 1]:
                continue
            cur_gas = gas[i]
            flag = 1
            next_pos = i
            while cur_gas >= cost[next_pos]:
                if flag == len(gas):
                    return i
                flag += 1
                cost_temp = cost[next_pos]
                next_pos = (next_pos + 1) % len(gas)
                cur_gas += gas[next_pos] - cost_temp
        return -1