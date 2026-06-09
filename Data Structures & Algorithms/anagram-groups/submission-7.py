from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            hashmap["".join(sorted(word))] += [word]
        
        return list(hashmap.values())