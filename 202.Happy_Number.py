class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        while n != 1 and n not in st:
            st.add(n)
            n = sum(int(i)**2 for i in str(n))

        return (True if n == 1 else False)
