def Missing_number(l):
    ''' here missing number from unsorted array so what we have to think about is eg. given list with 
    len(l) then actual list to identify the missing number will be len(l) +1..
    what I can think of right now is.. there are two ways this can be done..
    1. lets get the sum of n natural numbers from the list .. since it is mentioned as to no are unsorted but 
        starts from 0.. so then we can loop over the elements and get the sum as well and just take the subtraction w will have 
        missing number.
    2. Another simple way can be lets xor all the elements from list with the all the elements list made
       from range of 0 till len(l)+1 '''
    '''
    s=0
    summation =0
    for i in l:
        s = s+i
        #sum of elements from given list
    for j in range(0, len(l)+1):
        summation += j            
    missing_no =   summation -  s
    print(missing_no)

Missing_number([0,2,1,4,3,5,6,8])    '''

    s = sum(l)
    new = [x for x in range( len(l)+1)]
    summation = sum(new)
    miss = summation -s
    print(miss)

Missing_number([0,2,1,4,3,5,6,8]) 
