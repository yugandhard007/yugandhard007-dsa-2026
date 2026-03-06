original =[0,0,1,1,1,2,2,3,3,4]
def remove_duplicates(nums):
    ''' #First correct attempt
    arr =[]  
    for i in nums:
        if i not in arr:
            arr.append(i)
            
    for j in range(len(nums)):
        if j <= (len(arr)-1):
            nums[j] = arr[j]
        else:
            continue    
            
    return len(arr)   '''
    if not nums:
        return 0
    i = 0
    
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i] =nums[j]
    return i+1        

print(remove_duplicates(original))
