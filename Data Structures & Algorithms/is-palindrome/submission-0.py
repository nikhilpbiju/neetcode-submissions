class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=s.lower()
        ss=ss.replace(" ","")
        for c in ss:
            if c.isalnum():
                continue
            else:
                ss=ss.replace(c,"")
        
        print(ss)
        if ss==ss[::-1]:
            return True
        return False