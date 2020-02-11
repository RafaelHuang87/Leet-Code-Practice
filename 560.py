# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         import collections
#         n, d = len(nums), collections.defaultdict(int)
#         d[0] = 1
#         sum, res = 0, 0
#         for i in range(n):
#             sum += nums[i]
#             if sum - k in d:
#                 res += d[sum - k]
#             d[sum] += 1
#         return res



def hex2int(s_hex):
    return int(s_hex, 16)

# To achieve high mark, you need to write several functions to avoid
# repeated codes.

# Write your functions here (below this line)
# def format_hex(s_hex):
#     while len(s_hex) > 2:
#         if s_hex[0] == "0":
#             s_hex = s_hex[1:]
#         else:
#             break
#     return s_hex

def transform(input):
    temp = []
    res = "."
    for part in input:
        if not part.isdigit():
            temp.append(str(hex2int(part)))
        else:
            temp.append(str(int(part)))
    res1 = res.join(temp)
    return temp, res1

def validate(ip):
    if len(ip) != 4 or ip[0] != '10':
        return False
    for i in range(1, 4):
        if int(ip[i]) > 255 or int(ip[i]) < 0:
            return False
    return True
# Write your main code here (below this line)

ip_address = input("Enter IP address: ")
ip_list = ip_address.split(".")
flag = True
for part in ip_list:
    if len(part) < 2 or part.upper() not in "ABCDEF":
        flag = False
        break
if flag:
    ip_trans, ip = transform(ip_list)
    if validate(ip_trans):
        print(ip)
    else:
        print("IP address is not valid.")
else:
    print("IP address is not valid.")
