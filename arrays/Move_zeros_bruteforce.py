def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        new = list([0]*len(nums))
        l=[]
        for i in nums:
            if i!=0:
                l.append(i)
            else:
              continue

        l = l + new[len(l)-1:]      
        for i in range(len(l)-1):
            nums[i] = l[i]
        '''
        for i in range(len(l),len(nums)):
            nums[i] = new[i]'''
        print(nums)  
moveZeroes([0,1,0,3,12])
