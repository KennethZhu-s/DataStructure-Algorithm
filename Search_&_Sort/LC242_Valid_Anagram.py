"""
LC 242 Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

ex:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""


class Solution1:   # O(nlogn)
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        tt = list(t)
        ss.sort()
        tt.sort()

        return ss == tt


class Solution2:    # O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}  # i.e. {'a':1, 'b':2}

        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1
        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1

        return dict1 == dict2
