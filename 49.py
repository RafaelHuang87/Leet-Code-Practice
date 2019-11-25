class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        temp_dict=dict()
        for i in range(len(strs)):
            strsort = ''.join(sorted(strs[i]))
            if not strsort in temp_dict:
                temp_dict[strsort]=[i]
            else:
                temp_dict[strsort].append(i)
        res=[]
        for list1 in temp_dict.values():
            temp=[]
            for index in list1:
                temp.append(strs[index])
            res.append(temp)
        return res