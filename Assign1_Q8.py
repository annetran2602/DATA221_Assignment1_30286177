# Anne Tran (UCID 30286177)
# DATA 221_Assignment 1_ Q8

import pandas as pd
data={ # data
    "A":[1,2,2,1],
    "B":[3.1, 4.2, 1.5, 6.3],
    "C":[800,150,400,210]
}
df=pd.DataFrame(data)  # build
df["D"]=df["A"]+df["B"]+df["C"] # create new column & calculate the sum of column A, B and C

print(df)
