import numpy as np
nums = np.array([10,11,12,13,14])
print("Original array:")
print(nums)
x = int(input("First number :"))  
y = int(input("Last number : "))  
z = 5
new_nums = np.zeros(len(nums) + (len(nums)-1)*(z))
new_nums[::z+1] = nums
print("\nNew array:")
print(new_nums)
