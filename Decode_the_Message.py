class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic = {}
        st = "abcdefghijklmnopqrstuvwxyz"
        tem = ""
        for i in range(len(key)):
          if key[i] == ' ':
            continue
          if key[i] in tem:
            continue
          tem += key[i]
        space = " "
        for i in range(26):
          dic[tem[i]] = st[i]
        ans = ""
        for i in range(len(message)):
          if message[i] == ' ':
            ans += space
            continue
          ans += dic[message[i]]
        return (ans)



        