import numpy as np

# ************ 1 - D array ***********

a = np.array([1,2,3,4,5,6,7,8,9])
print(a)
print(f"It is a \'{a.ndim}-D\' array")
print(a.shape)
print("\n")

# ************ 2 - D array ***********

b = np.array([[1,2,3,4,5,6,7,8,9], 
              [11,12,13,14,15,16,17,18,19]])
print(b)
print(f"It is a \'{b.ndim}-D\' array")
print(f"It will show how many row and column is present in the array\'(rows, column)\'{b.shape} \n")

# ************ 3 - D array ***********

c = np.array([[[1,2,3,4,5,6,7,8,9],
               [11,12,13,14,15,16,17,18,19],
               [21,22,23,24,25,26,27,28,29]],
               [[31,32,33,34,35,36,37,38,39],
                [41,42,43,44,45,46,47,48,49],
                [51,52,53,54,55,56,57,58,59]]])
print(c)
print(f"It is a \'{c.ndim}-D\' array")
print(f"It will show how many row and column is present in the array\'(2-D array, rows, column)\'{c.shape}")
print(type(c))
print("\n")

# ************ indexing in 1-D array ***********

print("*****indexing in 1-D array*****")
print(a[5])
print ("\n")

# ************ indexing in 2-D array ***********

print("*****indexing in 2-D array*****")
print("[rows, column]=[1,4]"),
print(b[1,4])
print("\n")

# ************ indexing in 3-D array ***********

print("*****indexing in 3-D array*****")
print("[2-D array, rows, column]=[1,1,4]"),
print(c[1,1,4])
print("\n")

# ************ Slicing in 1-D array ***********

print("******slicing in 1-D array*****")
print(a[2:7+1])
print(a[2:8])
print("\n")

# ************ Slicing in 2-D array ***********

print("*****slicing in 2-D array*****")
print("[rows,starting index : ending index]")
print(b[1,2:8])
print("\n")

# ************ Slicing in 3-D array ***********

print("*****slicing in 3-D array*****")
print("[2-D array, rows, starting index : ending index]")
print(c[1,2,2:8])
print("\n")



# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a)
# print(type(a))
# b = np.mean(a)
# print(b)

# rows = int(input("how many rows you want: "))
# cols = int(input("how many columns you want: "))

# data = []

# for i in range (rows):
#     row = list(map(int, input(f"Row{i + 1}: ").split( ",")))
#     data.append(row)
#     arr = np.array(data)
#     print(arr)