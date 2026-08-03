class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #my solution, sum up the total amount of bananas
        #then divide by the hours allowed
        #give h is always greater than or equal to the length of piles


        def can_eat_all(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
            return total_hours

        L = 1
        R = max(piles)
        result = R

        while L <= R:
            mid = (L + R) // 2
            if can_eat_all(mid) <= h:
                result = mid
                R = mid - 1
            else:
                L = mid + 1
        return result