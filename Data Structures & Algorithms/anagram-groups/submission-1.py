class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newdict={}
        for n in strs:
            s = tuple(sorted(n))
            if s not in newdict:
                newdict[s] =[]
            newdict[s].append(n)
        return list(newdict.values())