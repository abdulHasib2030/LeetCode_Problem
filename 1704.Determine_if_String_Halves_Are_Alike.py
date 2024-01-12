class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)
        n = length//2
        left , right = 0,0
        
        for i in range(length):
            if s[i] == 'a' or s[i] == 'A' or s[i] == 'e' or s[i] == 'E' or s[i] == 'i' or s[i] == 'I' or s[i] == 'o' or s[i] == 'O' or s[i] == 'u' or s[i] == 'U':
                if n > i:
                    left +=1
                else:
                    right +=1
        if left == right:
            return (True)
        else:
            return (False)


        