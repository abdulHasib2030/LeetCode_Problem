class Solution:
    def reverse(self, x: int) -> int:
        k= ""
        temp = str(x)
        if temp[0] == '-':
            k += temp[0]
            k += temp[:0:-1]
            if 2147483648 > int(k) and -2147483647 < int(x):
                if -2147483647 > int(k):
                    return 0
                return (int(k))
            else:
                return (0)
        else:
            k = (temp[::-1])
            if 2147483648 > int(k) and -2147483647 < int(k):
                return (int(k))
            else:
                return (0)

        