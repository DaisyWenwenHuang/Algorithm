# https://leetcode.com/problems/hand-of-straights/
# leetcode 846
# medium
# greedy
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
			# check if the size of hand can be divided into equal groups with the groupsize 
            return False
		# hashmap to store the count of each number
        count = {}
        for ele in hand:
            count[ele] = 1 + count.get(ele,0)

		# using minheap datastructure as we select the minimum number each time to form a new group
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            
            for i in range(first,first+groupSize):
                if i not in count:
					# check if the new group can be formed
                    return False
                count[i] -= 1
                if count[i] == 0:
					# if using all count of certain number, need to pop that number out of the minheap
                    if i != minH[0]:
						# if the number that being used all /needs to be poped out of the  minheap is 
						# not the smallest number in the minheap, the next new group can not be formed
						# as all the numbers in each group need to be the consecutive
                        return False
                    heapq.heappop(minH)
        return True
        