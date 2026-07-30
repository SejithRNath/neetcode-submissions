class Solution:
    def isNStraightHand(self, hand: List[int], group: int) -> bool:
        if len(hand) % group:
            return False
        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num,num+group):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True
                
                

        