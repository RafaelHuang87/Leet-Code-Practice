class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator < 0 and denominator < 0:
            numerator, denominator = -numerator, -denominator
        u, a, b = (numerator < 0) ^ (denominator < 0), abs(numerator), abs(denominator)
        a = a % b
        if a == 0:
            return str(numerator // denominator)
        s = str(abs(numerator) // b) + '.'
        q, l = {}, []
        while a < b:
            a = a * 10
            l.append(a)
            q[a] = a // b
        a = a % b * 10
        while a not in q and a != 0:
            l.append(a)
            q[a] = a // b
            a = a % b
            a = a * 10
        for i in range(0, len(l)):
            if a == l[i]:
                s = s + '('
            s = s + str(q[l[i]])
        if '(' in s:
            s += ')'
        if u:
            s = '-' + s
        return s
