
from ast import List


def removeDuplicates(self, nums: List[int]) -> int:
    #start at index 0 since we are not worried about this number
    i = 0
    for j in range(1, len(nums)):

        # check if the next number is not the same as the current on at [i]
        if nums[i] != nums[j]:
            #move the i position forward
            i+=1
            #set this indexed position to the value since it is not a duplicate value
            nums[i] = nums[j]

    #return the ith position + 1 for length
    return i+1


def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    
    for i in range(0, len(prices)-1):
        # profit equals the buy - sell of the next day
        # so if the current day is less than tomorrow we can add the difference as a profit
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
            
    return profit


def plusOne(self, digits: List[int]) -> List[int]:
    end = len(digits) - 1

    while(end >= 0):
        if digits[end] == 9:
            digits[end] = 0
        else:
            digits[end] +=1
            return digits
        end -=1

    return [1] + digits