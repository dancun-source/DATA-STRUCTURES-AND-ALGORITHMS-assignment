# Represents STATIC Linear Data Structure (Fixed Size)
import array as arr

# Defining an array of integers with a fixed size/type
# In systems, this uses a contiguous block of memory
numbers = arr.array('i', [10, 20, 30, 40, 50])

print("Static Array elements:")
for x in numbers:
    print(x)
