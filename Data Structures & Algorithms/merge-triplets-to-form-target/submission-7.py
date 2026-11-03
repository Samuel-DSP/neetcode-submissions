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

        n = len(triplets)
        currTriplet = [0,0,0]
        for x,y,z in triplets:
            new_x, new_y,new_z = max(currTriplet[0],x), max(currTriplet[1],y), max(currTriplet[2],z)
            if new_x <= target[0] and new_y <= target[1] and new_z <= target[2]:
                currTriplet = [new_x,new_y,new_z]
        return currTriplet == target