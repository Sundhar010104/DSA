class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        vowels = "aeiouAEIOU"
        l = 0
        r = len(s) - 1

        while l<r:
            while l<r and chars[l] not in vowels:
                l +=1
            while l<r and chars[r] not in vowels:
                r -=1
            chars[l],chars[r] = chars[r],chars[l]
            l +=1
            r -=1
        return ''.join(chars)
    

        