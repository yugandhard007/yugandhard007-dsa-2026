class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum =nums[0]
        current_sum =nums[0]

        for num in nums[1:]:
            current_sum = max(current_sum + num,num)
            max_sum = max(max_sum, current_sum)

        return max_sum




        '''
        sum_sub_max_array =[nums[0]]
        for i in range(1,len(nums)):
            start_sum =nums[i-1]
            sum_array = [start_sum]
            for j in range(i,len(nums)):
                start_sum+=nums[j]
                sum_array.append(start_sum)
            sum_sub_max_array.append(max(sum_array))
            # print(sum_sub_max_array) 
            # print(f"nums: {nums}, sum_sub_max_array: {sum_sub_max_array}")
        maximum_sum = max(sum_sub_max_array)
        return maximum_sum
        '''