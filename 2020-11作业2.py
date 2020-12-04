#有一个非常大的数组，比如有1亿个数字，求出里面数字小于5000的数字数目。
import numpy as np
arr = np.random.randint(1,10000,size = int(1e8))
arr[arr<5000].size

#给定一个8X3的数组A和一个2X2的数组B，从A中找出满足条件的行，条件是B中每一行都有元素（至少一个）出现在A中这一行中?(不考虑B中每行元素顺序)(提示: np.where)
#e.g. B = [[3,1],[2,4]]，A = [[3,2,0],[0,1,5],...]，那么这个A的第一行，也就是[3,2,0]是符合要求的，因为包含了B中第一行[3,1]中的3，
#也包含第二行[2,4]中的2。但A的第二行[0,1,5]就不符合要求，因为只含有B中第一行的元素1，第二行[2,4]没有任何一个元素包含在[0,1,5]。
A = np.random.randint(0,5,(8,3)).tolist()
B = np.random.randint(0,5,(2,2)).tolist()
print(A)
print(B)
for i in A:
    if B[0][0] not in i and B[0][1] not in i:
        continue
    if B[1][0] not in i and B[1][1] not in i:
        continue
    print(i)






