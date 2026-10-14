class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = []
        for i in strs:
            sort.append("".join(sorted(i)))
        hash = {}
        result = []
        for n,i in enumerate(sort):
            if i in hash:
                hash[i].append(strs[n])
            else:
                hash[i] = [strs[n]]
        for i in hash:
            result.append(hash[i])
        return result
        