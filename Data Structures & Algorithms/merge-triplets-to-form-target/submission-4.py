class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # valid = []
        # a = b = c = False

        # for triplet in triplets:
        #     if all(triplet[j] <= target[j] for j in range(3)):
        #         valid.append(triplet)
        
        # for i in range(len(valid)):
        #     if valid[i][0] == target[0]:
        #         a = True
        #     if valid[i][1] == target[1]:
        #         b = True
        #     if valid[i][2] == target[2]:
        #         c = True

        # return a and b and c

        a = b = c = False

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                if x == target[0]:
                    a = True
                if y == target[1]:
                    b = True
                if z == target[2]:
                    c = True

        return a and b and c