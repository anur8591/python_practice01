import numpy as np

# ************ 1 - D array ***********

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
print(f"It is a \'{a.ndim}-D\' array")
print(a.shape)
print("\n")

# ************ 2 - D array ***********

b = np.array([[1,2,3,4,5,6,7,8,9,10], 
              [11,12,13,14,15,16,17,18,19,20]])
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

# ************ Reshaping array from 1-D to 2-D array ***********

print("*****Reshaping 1-D array to 2-D array*****")
x = a.reshape(2,6)
print("1-D array")
print(a)
print("2-D array")
print(f"{x}\n")

# ************ Reshaping array from 1-D to 3-D array ***********

print("*****Reshaping 1-D array to 3-D array*****")
y = a.reshape(2,2,3)
print("1-D array")
print(a)
print("3-D array")
print(f"{y}\n")

# ************ Reshaping array from 2-D to 1-D array ***********

print("***** Reshaping 2-D array to 1-D array *****")
d = b.reshape(1,20)
print("2-D array")
print(b)
print("1-D array")
print(f"{d}\n")

# ************ Reshaping array from 2-D to 3-D array ***********

print("***** Reshaping 2-D array to 3-D array *****")
e = b.reshape(2,2,5)
print("2-D array ")
print(b)
print("3-D array ")
print(f"{e}\n")

# ************ Generating number ***********

print("generating number for numpy")
a1 = np.random.randint(1,100, size = 100)
print(a1)
a2 = np.sort(a1)
print("order")
print(a2)
print("\n")

# ************ Find the missing value between 2 numbers  ***********

a3 = np.random.uniform(1,10, size = 7)
print(".uniform will return the value between the range given in decimal and unorderd like the range is 1-9 see:")
print(a3)
print("\n")

# ************ generating a unrepeated number using Numpy array  ***********

a4 = np.random.choice(np.arange(1,101),size=100, replace=False)
a5 = np.sort(a4)
print(a5)
print("\n")

# ************ number gussing game using Numpy   ***********

# a5 = np.random.randint(1,5)
# a6 = int(input("enter the number between 1 to 5: "))

# if a6 == a5:
#     pass
#     print("user won the game🎉🎊")
# else:
#     pass
#     print("user loose the game🥺 ")
# print("\n")


# ************ finding 'mean' using Numpy ***********

a7 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a8 = np.mean(a7)
print(a8)
print("\n")

# ************ finding 'median' using Numpy ***********

a8 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a9 = np.median(a8)
print(a9)
print("\n")

# ************ finding 'mode' using Numpy and statistic  ***********

import statistics as st 

b1 = np.array([1,2,3,4,5,6,7,8,9])
b2 = np.array([1,2,2,3,4,8,5,4,8,5,5,4,1,8,4,5,1,8,7,8,4,5,6,4,6,8,1,5,1,6,5,1,8,6,1,6,8])
b3 = st.mode(b1)
b4 = st.mode(b2)
print(f"if the number is unique the the mode is smallest number present in the array: {b3}")
print(b1)
print(f"the mode is{b1}")
print(b2)
print(f"the mode is {b4}")
print("\n")

# ************ Mathematical Operation on Numpy Array  ***********

x1 = np.array([1,2,3,4,5,6,8,7,9,10])
x2 = np.array([11,12,13,14,15,16,17,18,19,20])
print("Adding two Numpy array method 1 ")
z = x1 + x2
print(z)
print("Adding two numpy array method 2 ")
z1 = np.add(x1,x2)
print(z1)
print("concatenating two numpy array")
z2 = np.concatenate((x1,x2))
print(z2)
print("\n")

# ************ Performing Ascending and Decending Opperation ***********

print("performing ascending operation")
print("before ascending order")
z3 = np.random.choice(np.arange(1,16),size=15, replace=False)
print(z3)
z4 = np.sort(z3)
print("ascending order")
print(z4)
print("Decending order")
print(z4[::-1])


print("method 2 to find decending order array")
z5 = np.array([5,7,16,6,15,63,75,65])
z6 = np.sort(z5)
print(z6)
z7 = np.flip(z6)
print(z7)

# ************ create 1-D, 2-D, 3-D array with same number  ***********

print("1-D array with same number")
ab = np.full((4),5)
print(ab)
print("2-D array with same number")
abc = np.full((3,5),8)
print(abc)
print("3-D array with same number")
abcd = np.full((3,5,4),9)
print(abcd)
print("\n")

# ************ create 1-D, 2-D, 3-D array with same number  ***********

print("creating a numpy array by taking input form user: ")

# rows = int(input("how many rows you want: "))
# cols = int(input("how many columns you want: "))

# data = []

# for i in range (rows):
#     row = list(map(int, input(f"Row{i + 1}: ").split( ",")))
#     data.append(row)
#     arr = np.array(data)
#     print(arr)









#********************************* THE END **************************************