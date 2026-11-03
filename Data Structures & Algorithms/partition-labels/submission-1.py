class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq_map = Counter(s)
        result = []
        left, right = 0, 0
        current = set()

        while right < len(s):
            character = s[right]
            
            current.add(character)
            freq_map[character] -= 1
            if freq_map[character] == 0:
                current.remove(character)
            
            if len(current) == 0:
                result.append(right - left + 1)
                left = right + 1
            
            right += 1

        return result