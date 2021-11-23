lst = ([0, 1, 2, 3, 4, 5, 6, 7, 8])
def calculate(lst):
  import numpy as np
# base case
  if len(lst) != 9:
    return "List must contain 9 numbers"
# transforming list into matrix  
  x = np.array(lst).reshape(3, 3)
# finding mean
  r1 = x.mean(axis = 0)
  r2 = x.mean(axis = 1)
  r3 = x.mean()
  print("\nmean: ", r1, r2, r3)
# finding variance
  v1 = x.var(axis = 0)
  v2 = x.var(axis = 1)
  v3 = x.var()
  print("variance: ", v1, v2, v3)
# finding standard deviation
  s1 = x.std(0)
  s2 = x.std(1)
  s3 = x.std()
  print("standard deviation: ", s1, s2, s3)
# finding max
  m1 = x.max(0)
  m2 = x.max(1)
  m3 = x.max()
  print("max: ", m1, m2, m3)
# finding min
  min1 = x.min(0)
  min2 = x.min(1)
  min3 = x.min()
  print("min: ", min1, min2, min3)
# finding sum
  sum1 = x.sum(0)
  sum2 = x.sum(1)
  sum3 = x.sum()
  print("sum: ", sum1, sum2, sum3)

calculate(lst)