m=[0,1,3,4]

def missing_number(m):
  for i in range(min(m),max(m)+1):
    if i not in m:
      print(i)

missing_number(m)