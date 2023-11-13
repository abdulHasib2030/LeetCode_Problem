class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []
        for i in tokens:
            if i == '+':
                a, b = lst.pop(), lst.pop()
                lst.append(a+b)
            elif i == '-':
                a, b = lst.pop(), lst.pop()
                lst.append(b-a)
            elif i == '*':
                a, b = lst.pop(), lst.pop()
                lst.append( b * a )
            elif i == '/':
                a, b = lst.pop(), lst.pop()
                lst.append(int( b / a))
            else:
                lst.append(int(i))
        return lst.pop()
 