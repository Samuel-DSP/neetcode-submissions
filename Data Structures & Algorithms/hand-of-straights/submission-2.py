class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        cards = Counter(hand)
        for x in hand:
            if cards[x] != 0:
                cards[x] -= 1
                for i in range(1, groupSize):
                    y = x + i
                    if y not in cards or cards[y] == 0:
                        return False
                    cards[y] -= 1
        return True