class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n=len(machines)
        sm=sum(machines)
        if sm%n !=0: return -1
        target=sm//n
        cur=res=0
        for m in machines:
            res=max(res,m-target,abs(cur))
            cur+=m-target
        return res
