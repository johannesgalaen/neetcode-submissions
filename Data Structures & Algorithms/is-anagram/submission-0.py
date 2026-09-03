class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)
        s_dict = {}
        t_dict = {}

        for letter in s_list:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        for letter in t_list:
            t_dict[letter] = t_dict.get(letter, 0) + 1
        
        if s_dict == t_dict:
            return True
        else:
            return False
