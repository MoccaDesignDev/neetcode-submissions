from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
           freq1 = defaultdict(list)

           for word in strs:
               sorted_word = "".join(sorted(word))
               freq1[sorted_word].append(word)
           
           return list(freq1.values())
         