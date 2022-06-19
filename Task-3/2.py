import numpy as np

x = np.random.randint(1,3,5)
print("First array:")
print(x)

y = np.random.randint(1,3,5)
print("Second array:")
print(y)


array_equal = np.allclose(x, y)
print(array_equal)
