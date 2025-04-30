import pandas as pd


#********************* creating empty Series ******************

print("\n")
s = pd.Series()
print(f"{s}\n")

#********************* Creating Series from Array: ******************

data = [11,12,"Apple","B",55.55,"Banana"]
s1 = pd.Series(data)
print(s1)
print("\n")

#********************* how to remove dtype from the  ******************

print(s1.to_string(dtype=False))
print("\n")

#********************* how to remove default index from the label  ******************

print(s1.to_string(index = False))
print("\n")

#********************* how to add our own label in the place of default label  ******************

s2 = pd.Series(data, index = ["hello", "how", "are", "you", "I'm", "fine"])
print(s2.to_string(dtype=False))
print("\n")

#********************* how to access the value in series by using indexing operation ******************

print(s1[4])
print(s2["you"])
print("\n ")

#********************* performing slicing in pandas  ******************

print("performing slicing in pandas")
print(s1[2:6])
print("\n")
s3 = (s2["how":"I'm"])
s4 = (s3.to_string(dtype = False))
print(s4)
print("\n")

#********************* performing Data Frame  ******************

data1 = {"Name":["Anurag","Ankita","Suraj"], "Age":[19, 22, 25]}
s5 = pd.DataFrame(data1)
print(s5)