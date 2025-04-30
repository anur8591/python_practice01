import pandas as pd


#********************* creating empty Series ******************

print("\n")
s = pd.Series()
print(f"{s}\n")

#********************* Creating Series from Array: ******************

data = [11,12,"Apple","B",55.55,"Banana"]
s1 = pd.Series(data)
print(s1)

#********************* how to remove dtype from the  ******************