import sys
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        fstBuy,fstSell = -sys.maxsize,0
        secBuy,secSell = -sys.maxsize,0
        for i in prices:
            fstBuy = max(fstBuy, -i)
            fstSell = max(fstSell, fstBuy + i)
            secBuy = max(secBuy, fstSell - i)
            secSell = max(secSell, secBuy + i)
        return secSell
