from operator import xor


def Missing_Number(l):
    all_elements = [x for x in range(len(l)+1)]

    missing_no = 0
    for i in l:
      missing_no^=i
    for j in all_elements:
      missing_no^=j 

    print(missing_no)

Missing_Number([0,2,1,4,3,5,6,8]) 
