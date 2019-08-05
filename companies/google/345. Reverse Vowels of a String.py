class Solution:
    def reverseVowels(self, s: str) -> str:
        spt, ept = 0, len(s)-1
        result =[char for char in s] 
        vowels = ('a','e','i','o','u')
        while spt < ept:
            if not s[spt].lower() in vowels:
                spt += 1
            if not s[ept].lower() in vowels:
                ept -= 1
            
            if s[ept].lower() in vowels and s[spt].lower() in vowels:
                result[spt] = s[ept]
                result[ept] = s[spt]
                spt += 1 
                ept -= 1
        return ''.join(result)

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseVowels('hello'))
