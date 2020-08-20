import numpy as np

###### NUMPY ARRAYSSSSSSSSSSSSSSS
# x=[2,3,4,5,6]
# nums = np.array(x)
# nums = np.array([[2,4,6], [8,10,12], [14,16,18]])
#
# # arange(start, end[excluded], stepsize:default 1)
# nums = np.arange(2,7,2)
# # print(nums)
#
# zeros = np.zeros((5,4))
# ones = np.ones((5,4))
# # linspace(start, end[included], linearly-spaced numbers(equally spaced elements)
# # that you want between the specified range:default 50)
# lin=np.linspace(1,10, 20)
# # print(lin)
#
# # Identity matrix
# idn=np.eye(4)
# # print(idn)
# # random.rand::uniform distribution
# random = np.random.rand(2,3)
# # random.randn::Normal(Gaussian) distribution
# random = np.random.randn(2,3)
# # randint(lower bound, upper bound[excluded], number of integers to return)
# random = np.random.randint(50,60, 20)
# print(random)

#####################################################################################
# nums = np.arange(1,17)
# nums = nums.reshape(4,4)
# print(nums)

# random = np.random.randint(1,100,5)
# print(random.min()) #return element/value
# print(random.max())
# print(random.argmin()) #return position
# print(random.argmax())
# print(random)

# nums = np.arange(1,16)
# # print(nums[2:4])
# nums2= nums[0:8]
# print(nums2)

# nums = np.arange(1,10)
# nums2d = nums.reshape(3,3)
# print(nums2d)

# print(nums2d[2,2]) #Return element
# print(nums2d[2]) #Return row as array
# print(nums2d[:,2]) #Return column as array
# print(nums2d[1:,:2]) #Return row and columns as 2Darray

####### Arithmetic Operations with NumPy Arrays ######################################
# nums = np.arange(1,16)
# nums3 = (nums+nums+100-100)/2
# nums3 = np.log(nums)
# nums3 = np.exp(nums)
# nums3 = np.sqrt(nums)
# nums3 = np.sin(nums)
# print(nums3)

####### Linear Algebra Operations with NumPy Arrays #################################
# # Vectors/Array
# x = np.array([2,4])
# y = np.array([1,3])
# a = x*y
# print(a.sum())
# print(x.dot(y))

# # Matrices
# X = np.array(([1,2,3], [4,5,6]))
# Y = np.array(([1,2], [4,5], [7,8]))
# print(X.dot(Y))

# # Inverse of Matrix: Matrix*InverseMatrix=IdentityMatrix
# Y = np.array([[1,2],[3,4]])
# Z = np.linalg.inv(Y)
# print(Z)
# print(Y.dot(Z)) # Checking if inverse is right(Result will have diagonals 1)

# Trace of matrix::sum of all the elements in the diagonal
# X=np.array([[1,2,3], [4,5,6], [7,8,9]])
X=np.array(([1,2,3], [4,5,6], [7,8,9]))
print(np.trace(X))
Z = np.linalg.det(X) #Finding the Determinant of a Matrix
print(Z)