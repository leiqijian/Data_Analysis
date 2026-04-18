'''
Dataframe算术运算
    1. add() / +
    2. sub() / -
    3. mul() / *
    4. div() / /
    5. mod() / %
'''

import pandas as pd
import numpy as np

dataFrame = pd.DataFrame(np.random.randint(low=1, high=10, size=(3, 5)))
print(dataFrame)

# 1. add
dfAddAll =  dataFrame.add(100)
print(dfAddAll)

dfAdd =  dataFrame[0].add(100)
print(dfAdd)

print("----")

# 2. sub
dfSubAll =  dataFrame.sub(100)
print(dfSubAll)

dfSub =  dataFrame[0].sub(100)
print(dfSub)

print("----")

# 3. mul
dfMulAll =  dataFrame.mul(100)
print(dfMulAll)

dfMul =  dataFrame[0].mul(100)
print(dfMul)

print("----")

# 4. div
dfDivAll =  dataFrame.div(100)
print(dfDivAll)

dfDiv =  dataFrame[0].div(100)
print(dfDiv)
