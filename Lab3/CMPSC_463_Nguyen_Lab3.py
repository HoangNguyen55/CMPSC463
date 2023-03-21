class Solution:
    from random import randint
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # initialize variables
        # returning value
        finalPosition = -1
        # valid range
        low = 0
        high = len(nums) - 1

        # loop until we find the right position
        while finalPosition != len(nums) - k:
            # set the piviot as a random nth element
            pivot = randint(low, high)
            # switch the pivot with the last element in the valid range
            self.switchPosition(nums, pivot, high)
            i = high - 1
            # set the pivot's nth element to it's actual value
            pivot = nums[high]

            # loop though the valid range of the list, we go from high to low because we're looking for the kth LARGEST element
            for j in range(high - 1, low - 1, -1):
                # if number is hiher than the pivot switch them
                if nums[j] >= pivot:
                    if i != j:
                        self.switchPosition(nums, i, j)
                    # decrease i to move to the next unsorted item
                    i -= 1

            # switch the last element of the valid range (which is the pivot point) to finalPosition of the pivot point
            finalPosition = i + 1
            self.switchPosition(nums, high, finalPosition)        
            # if the position of the pivot point is higher than the kth largest element
            # then that mean the current pivot point is smaller in value than what we're looking for
            # so we discard everything lower than the pivot point
            if(len(nums) - finalPosition > k):
                low = i + 2
            # otherwise the position of the pivot point is lower
            # then that mean the current pivot point is bigger than what we're looking for
            # so we discard everything higher.
            # there is also a case that the final position is the same as what we're looking for
            # in that case the loop will terminate therefore this would have no nagative impact.
            else:
                high = finalPosition

        return pivot

    def switchPosition(self, nums: list[int], first:int, second:int):
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp