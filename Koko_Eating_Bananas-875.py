class Solution:
    def minEatingSpeed(self, piles, h) -> int:
        def can_eat(mid):
            actual_h = 0
            for pile in piles:
                actual_h += (pile+mid-1)//mid
            return actual_h <= h

        left = 0
        right = max(piles)
        while 1 < right-left:
            mid = (left+right) // 2
            if can_eat(mid):
              right = mid
            else:
              left = mid
        return right
      

        