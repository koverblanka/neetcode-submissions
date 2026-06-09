from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_as_list = list(s)
        t_as_list = list(t)

        print(Counter(s_as_list))
        print(Counter(t_as_list))

        return Counter(s_as_list) == Counter(t_as_list)
