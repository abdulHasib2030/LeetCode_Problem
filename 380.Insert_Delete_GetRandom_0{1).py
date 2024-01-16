import random
class RandomizedSet:

    def __init__(self):
        self.st = set()
        self.lst = []

    def insert(self, val: int) -> bool:
        if len(self.st) == 0 or val not in self.st:
            self.st.add(val)
            self.lst.append(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.st:
            self.lst.remove(val)
            self.st.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()