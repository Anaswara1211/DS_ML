import numpy as np
user_input = input("Enter numbers separated by a space: ")
arr = user_input.split()
# Convert list to numpy array
numpy_array = np.array(arr, dtype=float)
print(numpy_array)
# importing the modules
import numpy as np

k=int(input("Enter the value of k to find k'th smallest values:\n"))

# sorting the array
arr1 = np.sort(numpy_array)

# k smallest number of array
print(k, "smallest elements of the array")
print(arr1[:k])
