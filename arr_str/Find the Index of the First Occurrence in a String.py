class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range (len(haystack)):
            if (haystack[i] == needle[0]):
                 if needle == haystack[i:i+len(needle)]:        #check the window match
                    return i
        return -1
