''' Brute Force Approach:
def single_number(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i
    return None
'''
''' Hashmap Approach:
def single_number_hash(l):
  d ={}
  for i in l:
    d[i]= l.count(i)
  for i,j in d.items():
    if j == 1:
      return i
'''  
''' XOR Approach:'''
def single_number_xor(l):
  s = 0
  for i in l:
    s ^= i
  return s
print(single_number_xor([4,1,2,2,1]))