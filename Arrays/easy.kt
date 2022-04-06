import kotlin.math.max

fun removeDuplicates(nums: IntArray): Int {
    var i = 0

    for (j in 1..nums.size-1) {
        if (nums[i] != nums[j]) {
            i+=1
            nums[i] = nums[j]
        }
    }

    return i+1
}

fun maxSubArrayOfK(k: Int, nums: IntArray): Int {
    var max_sum = 0
    var window_sum = 0
    var window_start = 0
    
    if(nums.size == 1) {
        return nums[0]
    }

    for(i in 0..nums.size-1) {
        window_sum += nums[i]
        
        if (i >= k-1) {
            max_sum = max(max_sum, window_sum)
            window_sum -=nums[window_start]
            window_start++
        }

    }

    return max_sum